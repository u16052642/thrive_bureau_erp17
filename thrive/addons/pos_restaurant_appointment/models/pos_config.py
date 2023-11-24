  # -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    appointment_type_ids = fields.Many2many('appointment.type', string='Appointment Type')
