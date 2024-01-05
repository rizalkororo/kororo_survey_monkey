from odoo import models, fields


class SurveyMonkey(models.Model):
    _name = "survey.monkey"
    _description = "Survey Monkey Data"

    user = fields.Many2one("res.users", string="users",
                           default=lambda self: self.env.user)
    access_token = fields.Char()
    refresh_token = fields.Char()
