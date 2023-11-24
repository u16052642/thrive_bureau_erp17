# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    documents_hr_settings = fields.Boolean()
    documents_hr_folder = fields.Many2one('documents.folder', string="hr Workspace", check_company=True,
                                          default=lambda self: self.env.ref('documents_hr.documents_hr_folder',
                                                                            raise_if_not_found=False))
