# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive.tests.common import TransactionCase

from thrive.addons.hr_timesheet.tests.test_timesheet import TestCommonTimesheet


class TestHelpdeskTimesheetCommon(TestCommonTimesheet):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner = cls.env['res.partner'].create({
            'name': 'Customer Task',
            'email': 'customer@task.com',
        })

        cls.analytic_plan = cls.env['account.analytic.plan'].create({
            'name': 'Plan',
        })

        cls.analytic_account = cls.env['account.analytic.account'].create({
            'name': 'Analytic Account for Test Customer',
            'partner_id': cls.partner.id,
            'plan_id': cls.analytic_plan.id,
            'code': 'TEST',
        })

        cls.project = cls.env['project.project'].create({
            'name': 'Project',
            'allow_timesheets': True,
            'partner_id': cls.partner.id,
        })

        cls.helpdesk_team = cls.env['helpdesk.team'].create({
            'name': 'Test Team',
            'use_helpdesk_timesheet': True,
            'project_id': cls.project.id,
        })
