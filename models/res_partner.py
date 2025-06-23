from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_driver = fields.Boolean("Is Driver")
    is_helper = fields.Boolean("Is Helper")
    is_third_party_provider = fields.Boolean("Is Third Party Service Provider")