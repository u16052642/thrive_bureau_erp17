# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import api, models

class SaleOrderOption(models.Model):
    _inherit = 'sale.order.option'

    @api.depends('order_id.plan_id')
    def _compute_price_unit(self):
        super()._compute_price_unit()

    @api.depends('order_id.plan_id')
    def _compute_discount(self):
        super()._compute_discount()

    def _get_values_to_add_to_order(self):
        res = super()._get_values_to_add_to_order()
        if self.order_id.is_subscription:
            res.pop('discount')
        return res
