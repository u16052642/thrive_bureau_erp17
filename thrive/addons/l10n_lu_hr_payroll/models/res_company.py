# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'


    l10n_lu_official_social_security = fields.Char(string="Official Social Security")
    l10n_lu_seculine = fields.Char(string="SECUline number")
