# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'WhatsApp-Delivery',
    'category': 'Hidden/Tools',
    'description': """This module integrates Delivery with WhatsApp""",
    'depends': ['delivery', 'stock', 'whatsapp'],
    'data': [
        'data/whatsapp_template_data.xml'
    ],
    'license': 'OEEL-1',
    'auto_install': True
}
