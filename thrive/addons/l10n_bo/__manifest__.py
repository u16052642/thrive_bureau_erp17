# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'Bolivia - Accounting',
    'website': 'https://www.thrivebureau.com/documentation/17.0/applications/finance/fiscal_localizations.html',
    'icon': '/account/static/description/l10n.png',
    'countries': ['bo'],
    'version': '2.0',
    'description': """
Bolivian accounting chart and tax localization.

Plan contable boliviano e impuestos de acuerdo a disposiciones vigentes

    """,
    'author': 'Thrive / Cubic ERP',
    'category': 'Accounting/Localizations/Account Charts',
    'depends': [
        'account',
    ],
    'data': [
        'data/account_tax_report_data.xml',
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
