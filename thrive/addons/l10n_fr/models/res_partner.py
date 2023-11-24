# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
from thrive import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    siret = fields.Char(string='SIRET', size=14)
