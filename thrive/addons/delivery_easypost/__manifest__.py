# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
{
    'name': "Easypost Shipping",
    'description': "Send your parcels through Easypost and track them online",
    'category': 'Inventory/Delivery',
    'sequence': 315,
    'version': '1.0',
    'application': True,
    'depends': ['stock_delivery', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/delivery_carrier_views.xml',
        'views/res_config_settings_views.xml',
        'wizard/carrier_type_views.xml',
    ],
    'license': 'OEEL-1',
}
