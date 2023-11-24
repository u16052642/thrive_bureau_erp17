# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
from thrive import fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sendcloud_parcel_ref = fields.Json("Sendcloud Parcel Reference", copy=False) # List of : int (common shipping) or List<int> (multicollo shipping)
    sendcloud_return_parcel_ref = fields.Json("Sendcloud Return Parcel Ref", copy=False)
