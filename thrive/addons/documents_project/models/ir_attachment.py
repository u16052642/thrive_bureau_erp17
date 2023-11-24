# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.


from thrive import fields, models


class IrAttachment(models.Model):
    _inherit = ['ir.attachment']

    document_ids = fields.One2many('documents.document', 'attachment_id')
