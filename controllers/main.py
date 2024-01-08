from odoo import http as odooHttp
from odoo import exceptions
from odoo.http import request
from http.client import HTTPSConnection
import requests
from werkzeug.utils import redirect
from urllib.parse import urlencode
from odoo.exceptions import UserError
import json


class SuveyMonkeyLoginApi(odooHttp.Controller):

    _SM_API_BASE = "https://api.surveymonkey.com"
    _AUTH_CODE_ENDPOINT = "/oauth/authorize"
    _ACCESS_TOKEN_ENDPOINT = "/oauth/token"
    _SECRET = "185612692778930003729201491314498602691"
    _CLIENT_ID = "3nxJxzzLQW6-RFcheoIo0w"
    _HOME_URL = 'http://127.0.0.1:8080/'
    _REDIRECT_URL = "http://127.0.0.1:8080/kororo/survey-monkey-response"
    _CURRENT_PROFILE_URL = _HOME_URL + 'kororo/survey-monkey-response/users'

    def conn(self, **kwargs) -> HTTPSConnection:
        """
        Return secure connection of Https from
        surveymonkey
        """
        return HTTPSConnection("api.surveymonkey.com")

    def headers(self, access_token: str, **kwargs) -> dict:
        """
        Returning headers with token
        """
        return {
            'Accept': "application/json",
            'Authorization': f"Bearer {access_token}"
        }

    @odooHttp.route('/kororo/survey-monkey/', website=True, auth='public')
    def login(self, **kwargs):
        """
        Login endpoint to gain access to Survey monkey OAuth2.
        This will redirect to Survey monkey page with access_code
        """
        url_params = urlencode({
            "redirect_uri": self._REDIRECT_URL,
            "client_id": self._CLIENT_ID,
            "response_type": "code",
            "state": 200
        })

        # We hit the endpoint as per documentation and save the redirect url response in OAuthURL_AccessRequest
        OAuthURL = self._SM_API_BASE + self._AUTH_CODE_ENDPOINT + "?" + url_params
        return redirect(OAuthURL)

    @odooHttp.route('/kororo/survey-monkey-response', website=True, auth='user')
    def exchange_code_for_token(self, code=None, **kwargs):
        """
        After redirection with above function, the autentication code on address url bar
        must be caught and we use it to return access token from surveymonkey.
        """
        if code:
            data = {
                "client_secret": self._SECRET,
                "code": code,
                "redirect_uri": self._REDIRECT_URL,
                "client_id": self._CLIENT_ID,
                "grant_type": "authorization_code"
            }

            access_token_uri = self._SM_API_BASE + self._ACCESS_TOKEN_ENDPOINT
            access_token_response = requests.post(access_token_uri, data=data)
            access_json = access_token_response.json()

            # If authenticated, we need the way to store survey monkey
            # access token to our odoo database.
            if "access_token" in access_json:

                survey_monkey_model = request.env['survey.monkey']

                # check if previous token exist in database.
                # if exist update db with new generated token
                data_exist = survey_monkey_model.search(
                    [('user', '=', request.uid)])
                if data_exist:
                    data_exist.access_token = access_json['access_token']

                # else create and save new token
                else:
                    data = {
                        'access_token': access_json['access_token']
                    }

                    survey_monkey_model.create(data)

                # after creating token and store it in odoo db
                # do some action to save it and get user profile
                response = requests.get(self._CURRENT_PROFILE_URL)

                if response.status_code == 200:
                    return redirect(self._HOME_URL + 'web')

            raise UserError("Authentication to Survey Monkey is failed.")

        raise UserError("You are not authorized to access this page!")

    @odooHttp.route('/kororo/survey-monkey-response/users', auth='user', website=True)
    def get_user_profile(self, **kwargs):
        """
        Here we try to retrieve user profile information
        from surveymonkey
        """
        token = request.env['survey.monkey'].search(
            [('user.id', '=', request.uid)]).access_token

        # initialize survey monkey profile db
        profile = request.env['survey.monkey.profile']

        if token:
            conn = self.conn()
            conn.request(
                "GET", "/v3/users/me", headers=self.headers(token))
            res = conn.getresponse()
            data = res.read().decode('utf-8')
            json_data = json.loads(data)

            # add profile_id to dict
            json_data['profile_id'] = json_data['id']

            # removing the rest
            json_data.pop('id')
            json_data.pop('question_types')
            json_data.pop('scopes')
            json_data.pop('sso_connections')
            json_data.pop('features')
            json_data.pop('href')

            # save in database
            profile.create(json_data)
            return

        raise exceptions.UserError("You have no access right")
