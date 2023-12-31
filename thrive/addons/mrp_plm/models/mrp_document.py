# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class MrpDocument(models.Model):
    _inherit = 'mrp.document'

    origin_attachment_id = fields.Many2one('ir.attachment')
