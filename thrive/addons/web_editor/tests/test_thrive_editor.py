# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import thrive.tests

@thrive.tests.tagged("post_install", "-at_install")
class TestThriveEditor(thrive.tests.HttpCase):

    def test_thrive_editor_suite(self):
        self.browser_js('/web_editor/tests', "", "", login='admin', timeout=1800)
