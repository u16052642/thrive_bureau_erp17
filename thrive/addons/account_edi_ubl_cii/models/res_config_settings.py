# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_is_ubl_cii = fields.Boolean(string='Peppol format', related='company_id.invoice_is_ubl_cii', readonly=False)
