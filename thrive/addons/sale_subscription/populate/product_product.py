# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models
from thrive.tools import populate


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _populate_factories(self):

        def is_recurring(values, counter, random):
            if values['type'] == 'service':
                return random.choices([True, False], [0.5, 0.5])[0]
            else:
                return False

        return super()._populate_factories() + [
            ('recurring_invoice', populate.compute(is_recurring))
        ]
