# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
from thrive import models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _get_name_invoice_report(self):
        if self.company_id.account_fiscal_country_id.code == 'AU':
            return 'l10n_au.report_invoice_document'
        return super()._get_name_invoice_report()
