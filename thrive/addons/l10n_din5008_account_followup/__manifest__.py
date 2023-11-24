# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'DIN 5008 - Payment Follow-up Management',
    'version': '1.0',
    'category': 'Accounting/Localizations',
    'author': 'Thrive Bureau ERP',
    'depends': [
        'l10n_din5008',
        'account_followup',
    ],
    'assets': {
        'web.report_assets_common': [
            'l10n_din5008_account_followup/static/src/**/*',
        ],
    },
    'auto_install': True,
    'license': 'OEEL-1',
}
