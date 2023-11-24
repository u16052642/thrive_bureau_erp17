# coding: utf-8
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class PosPaymentMethod(models.Model):
    _inherit = 'pos.payment.method'

    def _get_payment_terminal_selection(self):
        return super()._get_payment_terminal_selection() + [('six_iot', 'SIX IOT')]
