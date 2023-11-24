# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Indonesian - Accounting',
    'icon': '/account/static/description/l10n.png',
    'countries': ['id'],
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """
This is the latest Indonesian Thrive localisation necessary to run Thrive accounting for SMEs with:
=================================================================================================
    - generic Indonesian chart of accounts
    - tax structure""",
    'author': 'vitraining.com',
    'website': 'https://www.thrivebureau.com/documentation/17.0/applications/finance/fiscal_localizations/indonesia.html',
    'depends': [
        'account',
        'base_iban',
        'base_vat',
    ],
    'data': [
        'data/account_tax_template_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
