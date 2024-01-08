
from odoo import exceptions, models, fields, api
from xml import etree

_CREATE_URL = "http://127.0.0.1:8080/kororo/survey-monkey/"


class SurveyMonkey(models.Model):
    _name = "survey.monkey"
    _description = "Survey Monkey Data"

    user = fields.Many2one("res.users", string="users",
                           default=lambda self: self.env.user)
    access_token = fields.Char()
    refresh_token = fields.Char()

    def retrieve_surveymonkey(self):

        if self.user:
            return {
                'type': 'ir.actions.act_url',
                'url': _CREATE_URL,
                'target': 'new'
            }

    @api.model
    def create(self, vals):
        current_user_exist = self.env['survey.monkey'].search(
            [('user', '=', vals.get('user'))])

        db_records = self.env['survey.monkey'].search([])
        is_allowed = len(db_records) < 1

        # Allow user to create if no record in db
        # and only for it's self
        if current_user_exist:
            raise exceptions.UserError(
                "Only one record allowed for current user.")

        # if record more than one, discard it
        if not is_allowed:
            raise exceptions.UserError(
                "You cannot create record for another user.")

        return super(SurveyMonkey, self).create(vals)


class SurveyMonkeyProfile(models.Model):
    _name = "survey.monkey.profile"
    _description = "Survey Monkey Profile"

    user = fields.Many2one("res.users", string="users",
                           default=lambda self: self.env.user)
    profile_id = fields.Char()
    username = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    language = fields.Char()
    email = fields.Char(required=True)
    email_verified = fields.Boolean(default=False)
    account_type = fields.Char()
    date_created = fields.Char()
    date_last_login = fields.Char()
