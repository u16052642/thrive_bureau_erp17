# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models
from thrive.osv.expression import OR


class PosSession(models.Model):
    _inherit = 'pos.session'

    crm_team_id = fields.Many2one('crm.team', related='config_id.crm_team_id', string="Sales Team", readonly=True)

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['domain'] = OR([result['search_params']['domain'], [('id', '=', self.config_id.down_payment_product_id.id)]])
        result['search_params']['fields'].extend(['invoice_policy', 'type'])
        return result
