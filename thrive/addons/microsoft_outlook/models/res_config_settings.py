# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    microsoft_outlook_client_identifier = fields.Char('Outlook Client Id', config_parameter='microsoft_outlook_client_id')
    microsoft_outlook_client_secret = fields.Char('Outlook Client Secret', config_parameter='microsoft_outlook_client_secret')
