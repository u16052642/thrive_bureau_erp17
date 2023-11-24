# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models

class Pricelist(models.Model):
    _inherit = "product.pricelist"

    def _enable_rental_price(self, *args, **kwargs):
        """ Override to force the computation through rental price from website """
        return super()._enable_rental_price(*args, **kwargs) or self.env.context.get('website_id')
