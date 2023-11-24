# -*- encoding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 Noviat nv/sa (www.noviat.be). All rights reserved.

from thrive import fields, models


class AccountBankStatement(models.Model):
    _inherit = 'account.bank.statement'

    coda_note = fields.Text('CODA Notes')
