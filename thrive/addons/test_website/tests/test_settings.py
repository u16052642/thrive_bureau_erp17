# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import thrive
import thrive.tests

@thrive.tests.tagged('-at_install', 'post_install')
class TestWebsiteSettings(thrive.tests.HttpCase):
    def test_01_multi_website_settings(self):
        self.env['website'].create({'name': "Website Test Settings", 'specific_user_account': True})
        self.start_tour("/web", 'website_settings_m2o_dirty', login="admin")
