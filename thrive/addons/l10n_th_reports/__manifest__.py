# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

{
    "name": "Thailand - Accounting Reports",
    'countries': ['th'],
    "author": "Thrive PS",
    "version": "1.0",
    'category': 'Accounting',
    "description": """
Accounting reports for Thailand
==============================================================================
    """,
    "depends": [
        "l10n_th",
        "account_reports",
    ],
    "data": [
        "data/account_tax_report_data.xml",
    ],
    'auto_install': True,
    'installable': True,
    'license': 'OEEL-1',
}
