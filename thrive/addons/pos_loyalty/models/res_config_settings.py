# -*- coding: utf-8 -*-

from thrive import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_gift_card_settings = fields.Selection(related='pos_config_id.gift_card_settings', readonly=False)
