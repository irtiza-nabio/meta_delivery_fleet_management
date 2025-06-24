from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vehicle_id = fields.Many2one('fleet.vehicle')
    driver_id = fields.Many2one('res.partner', domain="[('is_driver', '=', True)]")
    helper_id = fields.Many2one('res.partner', domain="[('is_helper', '=', True)]")
    provider_id = fields.Many2one('res.partner', domain="[('is_third_party_provider', '=', True)]")
    provider_mobile = fields.Char(
        related="provider_id.mobile",
        store=True,
        readonly=True,
    )

    start_time = fields.Datetime("Start Time")
    end_time = fields.Datetime("End Time")
    total_delivery_time = fields.Char("Total Delivery Time", compute="_compute_total_time", store=True)

    delivery_method = fields.Selection([
        ('internal_delivery', 'Internal Delivery'),
        ('external_delivery', 'External Delivery'),
    ], string="Delivery Method")

    @api.depends('start_time', 'end_time')
    def _compute_total_time(self):
        for record in self:
            if record.start_time and record.end_time:
                diff = record.end_time - record.start_time
                record.total_delivery_time = str(diff)
            else:
                record.total_delivery_time = ''
