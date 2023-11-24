# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Field Service Reports',
    'category': 'Hidden',
    'summary': 'Create Reports for Field service workers',
    'description': """
Create Reports for Field Service
================================

""",
    'depends': ['worksheet', 'industry_fsm', 'web_studio'],
    'data': [
        'security/industry_fsm_report_security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/project_portal_templates.xml',
        'views/project_sharing_views.xml',
        'report/project_task_burndown_chart_report_views.xml',
        'report/worksheet_custom_report_templates.xml',
        'report/worksheet_custom_reports.xml',
        'data/fsm_report_data.xml',
        'data/mail_template_data.xml',
    ],
    'demo': ['data/fsm_report_demo.xml'],
    'post_init_hook': 'post_init',
    'auto_install': ['industry_fsm', 'web_studio'],
    'assets': {
        'web.assets_backend': [
            'industry_fsm_report/static/src/js/tours/industry_fsm_report_tour.js',
        ],
        'web.assets_frontend': [
            'industry_fsm_report/static/src/js/tours/industry_fsm_report_tour.js',
        ],
    },
    'license': 'OEEL-1',
}
