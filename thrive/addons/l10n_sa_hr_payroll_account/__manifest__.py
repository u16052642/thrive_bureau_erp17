# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
{
    'name': 'K.S.A. - Payroll with Accounting',
    'countries': ['sa'],
    'author': 'Thrive',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
Accounting Data for KSA Payroll Rules.
=======================================================

    """,
    'depends': ['hr_payroll_account', 'l10n_sa', 'l10n_sa_hr_payroll'],
    'data': [
        'data/account_chart_template_data.xml',
    ],
    'license': 'OEEL-1',
    'auto_install': True,
}
