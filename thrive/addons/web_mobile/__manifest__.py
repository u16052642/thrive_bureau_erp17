# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mobile',
    'category': 'Hidden',
    'summary': 'Thrive Mobile Core module',
    'version': '1.0',
    'description': """
This module provides the core of the Thrive Mobile App.
        """,
    'depends': [
        'web_enterprise',
    ],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'web_mobile/static/src/**/*',
        ],
        'web.tests_assets': [
            'web_mobile/static/tests/helpers/**/*',
        ],
        'web.qunit_mobile_suite_tests': [
            'web_mobile/static/tests/*_mobile_tests.js',
        ],
    },
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
