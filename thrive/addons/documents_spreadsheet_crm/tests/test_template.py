# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import thrive
from thrive.tests import tagged
from thrive.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestSpreadsheetTemplate(HttpCase):

    def test_insert_pivot_in_spreadsheet(self):
        self.start_tour('/web', 'insert_crm_pivot_in_spreadsheet', login='admin')
