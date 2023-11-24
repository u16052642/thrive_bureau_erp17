# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    documents_spreadsheet_folder_id = fields.Many2one(
        'documents.folder', related='company_id.documents_spreadsheet_folder_id', readonly=False)
