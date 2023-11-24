# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import _, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amazon_order_ref = fields.Char(
        string="Amazon Reference", help="The Amazon-defined order reference.", readonly=True
    )
    amazon_channel = fields.Selection(
        string="Fulfillment Channel",
        selection=[('fbm', "Fulfillment by Merchant"), ('fba', "Fulfillment by Amazon")],
    )

    _sql_constraints = [(
        'unique_amazon_order_ref',
        'UNIQUE(amazon_order_ref)',
        "There can only exist one sale order for a given Amazon Order Reference."
    )]

    def _action_cancel(self):
        out_of_sync_orders = self.env[self._name]
        if self.env.context.get('canceled_by_amazon'):
            for order in self:
                picking = self.env['stock.picking'].search(
                    [('sale_id', '=', order.id), ('state', '=', 'done')]
                )
                if picking:
                    # The picking was processed on Thrive while Amazon canceled it.
                    order.message_post(
                        body=_(
                            "The order has been canceled by the Amazon customer while some"
                            "products have already been delivered. Please create a return for this "
                            "order to adjust the stock."
                        )
                    )
                    out_of_sync_orders |= order
        return super(SaleOrder, self - out_of_sync_orders)._action_cancel()
