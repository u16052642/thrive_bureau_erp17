# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Peru - Accounting Reports',
    'countries': ['pe'],
    "description": """
Electronic accounting reports
    - Sales report
    - Purchase report

P&L + balance Sheet
    """,
    "version": "1.0",
    "author": "Vauxoo, Thrive Bureau ERP",
    "category": "Accounting/Localizations/Reporting",
    "website": "https://www.thrivebureau.com/app/accounting",
    "license": "OEEL-1",
    "depends": [
        "l10n_pe_edi",
        "account_reports",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/balance_sheet.xml",
        "data/profit_loss.xml",
        "data/account_ple_purchase_8_1_report.xml",
        "data/account_ple_purchase_8_2_report.xml",
        "data/account_ple_sales_14_1_report.xml",
        "data/l10n_pe.ple.usage.csv",
        "data/res.country.csv",
        "views/account_move_view.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "auto_install": True,
}
