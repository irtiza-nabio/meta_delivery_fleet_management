from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vehicle_id = fields.Many2one('fleet.vehicle', string="Vehicle")
    driver_id = fields.Many2one('res.partner', string="Driver", domain="[('is_driver', '=', True)]")
    helper_id = fields.Many2one('res.partner', string="Helper", domain="[('is_helper', '=', True)]")
    provider_id = fields.Many2one('res.partner', domain="[('is_third_party_provider', '=', True)]")
    provider_mobile = fields.Char(
        related="provider_id.mobile",
        store=True,
        readonly=True,
    )

    start_time = fields.Datetime("Start Time")
    end_time = fields.Datetime("End Time")
    total_delivery_time = fields.Char("Total Delivery Time", compute="_compute_total_time", store=True)

    def action_start_delivery(self):
        for record in self:
            record.start_time = fields.Datetime.now()

    def action_end_delivery(self):
        for record in self:
            if not record.start_time:
                raise UserError("Please start the delivery first.")
            record.end_time = fields.Datetime.now()

    @api.depends('start_time', 'end_time')
    def _compute_total_time(self):
        for record in self:
            if record.start_time and record.end_time:
                diff = record.end_time - record.start_time
                record.total_delivery_time = str(diff)
            else:
                record.total_delivery_time = ''