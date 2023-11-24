# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_ch_post_box = fields.Char(
        related="company_id.l10n_ch_post_box",
        readonly=False)
    l10n_ch_uid = fields.Char(
        related="company_id.l10n_ch_uid",
        readonly=False)
