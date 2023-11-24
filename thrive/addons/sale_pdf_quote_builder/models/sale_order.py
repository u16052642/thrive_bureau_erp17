# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _filter_product_documents(self, documents):
        return (
            super()._filter_product_documents(documents)
            | documents.filtered(lambda document: document.attached_on == 'inside')
        )
