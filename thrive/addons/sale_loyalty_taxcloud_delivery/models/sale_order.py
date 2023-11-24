# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from .taxcloud_request import TaxCloudRequest
from thrive import api, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _get_TaxCloudRequest(self, api_id, api_key):
        return TaxCloudRequest(api_id, api_key)
