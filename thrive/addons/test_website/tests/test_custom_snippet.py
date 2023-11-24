# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import thrive.tests
from thrive.tools import mute_logger


@thrive.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(thrive.tests.HttpCase):

    @mute_logger('thrive.addons.http_routing.models.ir_http', 'thrive.http')
    def test_01_run_tour(self):
        self.start_tour(self.env['website'].get_client_action_url('/'), 'test_custom_snippet', login="admin")
