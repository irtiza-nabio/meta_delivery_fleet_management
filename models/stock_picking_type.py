from odoo import models, fields, api

class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    delivery_subtype = fields.Selection([
        ('internal_delivery', 'Internal Delivery'),
        ('external_delivery', 'External Delivery'),
    ], string="Delivery Subtype")


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    delivery_subtype = fields.Selection([
        ('internal_delivery', 'Internal Delivery'),
        ('external_delivery', 'External Delivery'),
    ], string="Delivery Subtype", compute='_compute_delivery_subtype', store=True)

    delivery_started = fields.Boolean(
        compute='_compute_delivery_started',
        store=True
    )

    @api.depends('picking_type_id.delivery_subtype')
    def _compute_delivery_subtype(self):
        for rec in self:
            rec.delivery_subtype = rec.picking_type_id.delivery_subtype or False

    @api.depends('start_time')
    def _compute_delivery_started(self):
        for rec in self:
            rec.delivery_started = bool(rec.start_time)
