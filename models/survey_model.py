
from odoo import exceptions, models, fields, api

_CREATE_URL = "http://127.0.0.1:8080/kororo/survey-monkey/"


class SurveyMonkey(models.Model):
    _name = "survey.monkey"
    _description = "Survey Monkey Data"

    user_data = fields.Many2one("res.users", string="user",
                                default=lambda self: self.env.user)
    profile = fields.One2many("survey.monkey.profile", "survey_ids")
    access_token = fields.Char()
    refresh_token = fields.Char()
    email = fields.Char(default=lambda self: self.env.user.company_id.email)

    def retrieve_surveymonkey(self):

        if self.user_data:
            return {
                'type': 'ir.actions.act_url',
                'url': _CREATE_URL,
                'target': 'new'
            }

    @api.model
    def create(self, vals):
        current_user_exist = self.env['survey.monkey'].search(
            [('user_data', '=', vals.get('user_data'))])
        allowed = len(current_user_exist) < 1

        # Allow user to create if no record in db
        # and only for it's self
        if current_user_exist and not allowed:
            raise exceptions.UserError(
                "Only one record allowed for current user.")

        # if create another user record, then discard it
        if vals.get('user_data') != self.env.uid:
            raise exceptions.UserError(
                "You cannot create record for another user.")

        return super(SurveyMonkey, self).create(vals)

    def write(self, vals):
        """
        Update record in database
        """
        # prevent user to change user
        if vals.get('user_data') and vals.get('user_data') != self.env.uid:
            raise exceptions.UserError(
                "You cannot assign record for another user.")
        return super(SurveyMonkey, self).write(vals)


class SurveyMonkeyProfile(models.Model):
    _name = "survey.monkey.profile"
    _description = "Survey Monkey Profile"

    survey_ids = fields.Many2one(
        "survey.monkey", string="Survey ID", ondelete="cascade", index=True)
    profile_id = fields.Char(string="Profile ID")
    username = fields.Char()
    first_name = fields.Char()
    last_name = fields.Char()
    language = fields.Char()
    email = fields.Char(required=True)
    email_verified = fields.Boolean(default=False)
    account_type = fields.Char()
    date_created = fields.Char()
    date_last_login = fields.Char()
    sequence = fields.Integer('Sequence', default=1,
                              help="Used to order stages. Lower is better.")
