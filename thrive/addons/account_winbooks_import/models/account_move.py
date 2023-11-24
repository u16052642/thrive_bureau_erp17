# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    # technical field used to reconcile the journal items in Thrive as they were in Winbooks
    winbooks_matching_number = fields.Char(help="Matching number that was used in Winbooks")
    winbooks_line_id = fields.Char(help="Line ID that was used in Winbooks")
