# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive.tests import tagged
from thrive.tests.common import HttpCase


@tagged("post_install", "-at_install")
class TestSpreadsheetMultipage(HttpCase):
    def test_01_spreadsheet_save_multipage(self):
        self.start_tour("/web", "spreadsheet_save_multipage", login="admin")
