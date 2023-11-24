# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_header = fields.Binary(related='company_id.sale_header', readonly=False)
    sale_header_name = fields.Char(related='company_id.sale_header_name')
    sale_footer = fields.Binary(related='company_id.sale_footer', readonly=False)
    sale_footer_name = fields.Char(related='company_id.sale_footer_name')
