# -*- coding: utf-8 -*-

from thrive import models


class AccountPayment(models.Model):
    _inherit = "account.payment"

    def _get_whatsapp_safe_fields(self):
        return {'partner_id.mobile', 'currency_id.symbol'}
