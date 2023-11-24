#-*- coding:utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
from thrive import models, api, _
from thrive.exceptions import UserError


class AccountJournal(models.Model):
    _inherit = "account.journal"

    @api.ondelete(at_uninstall=False)
    def _prevent_unlink_payroll_journal(self):
        payroll_journals = self.env['hr.payroll.structure'].sudo().search([]).journal_id
        if self & payroll_journals:
            raise UserError(_("You cannot delete the journal linked to a Salary Structure"))
