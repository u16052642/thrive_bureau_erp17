# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from datetime import timedelta
from markupsafe import Markup

from thrive import fields
from thrive.addons.sms.tests.common import SMSCommon
from thrive.addons.test_mail_sms.tests.common import TestSMSRecipients
from thrive.tests.common import users
from thrive.tests import tagged
from thrive.tools import mute_logger


@tagged('mail_activity')
class TestActivity(SMSCommon, TestSMSRecipients):

    @classmethod
    def setUpClass(cls):
        super(TestActivity, cls).setUpClass()

        cls.test_record_voip = cls.env['mail.test.activity.bl.sms.voip'].create({
            'name': 'Test Record',
            'customer_id': cls.partner_1.id,
            'email_from': cls.partner_1.email,
            'phone_nbr': '0456999999',
        })

        cls.phonecall_activity = cls.env.ref('mail.mail_activity_data_call')
        cls.phonecall_activity.write({
            'default_user_id': cls.user_admin.id,
            'default_note': 'Test Default Note',
            'summary': 'Test Default Summary',
        })

        # clean db to ease tests
        cls.env['mail.activity.type'].search([
            ('category', '=', 'phonecall'),
            ('id', '!=', cls.phonecall_activity.id),
        ]).unlink()

    def test_activity_data(self):
        """ Ensure initial data for tests """
        self.assertEqual(self.partner_1.mobile, '0456001122')
        self.assertTrue(self.phonecall_activity)
        self.assertEqual(self.phonecall_activity.category, 'phonecall')

    @users('employee')
    @mute_logger('thrive.addons.voip.models.voip_queue_mixin')
    def test_create_call_activity(self):
        record = self.test_record_voip.with_env(self.env)

        activity = record.create_call_activity()
        self.assertEqual(activity.activity_type_id, self.phonecall_activity)
        self.assertFalse(activity.phone)
        self.assertEqual(activity.mobile, self.partner_1.mobile)
        self.assertFalse(activity.note)
        self.assertFalse(activity.summary)

        phonecall_activities = self.env['mail.activity'].sudo().search([
            ('activity_type_id', '=', self.phonecall_activity.id),
        ])
        phonecall_activities.write({'activity_type_id': False})
        self.phonecall_activity.unlink()

        # no more phonecall activity -> will be dynamically created
        self.assertFalse(self.env['mail.activity.type'].search([('category', '=', 'phonecall')]))
        activity = record.create_call_activity()
        new_activity_type = self.env['mail.activity.type'].search([('category', '=', 'phonecall')])
        self.assertTrue(bool(new_activity_type))
