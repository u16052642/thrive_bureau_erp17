# -*- coding: utf-8 -*-

from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sdworx_code = fields.Char(
        related='company_id.sdworx_code',
        readonly=False)
