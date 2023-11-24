# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    l10n_ch_post_box = fields.Char(string="Post Box")
    l10n_ch_uid = fields.Char(string="Identification Number (IDE-OFS)")
