# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_whatsapp_safe_fields(self):
        return {'partner_id.name', 'name', 'company_id.name', 'currency_id.symbol', 'amount_total', 'portal_url'}
