# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    fec_matching_number = fields.Char(help="Matching code that is used in FEC import for reconciliation")
