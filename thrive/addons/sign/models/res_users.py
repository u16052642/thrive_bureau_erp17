# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    sign_signature = fields.Binary(string="Digital Signature", copy=False, groups="base.group_system")
    sign_initials = fields.Binary(string="Digital Initials", copy=False, groups="base.group_system")
    sign_signature_frame = fields.Binary(string="Digital Signature Frame", copy=False, groups="base.group_system")
    sign_initials_frame = fields.Binary(string="Digital Initials Frame", copy=False, groups="base.group_system")
