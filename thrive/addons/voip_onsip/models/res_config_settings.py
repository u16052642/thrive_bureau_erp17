# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    wsServer = fields.Char(default="wss://edge.sip.onsip.com", config_parameter="voip.wsServer")
