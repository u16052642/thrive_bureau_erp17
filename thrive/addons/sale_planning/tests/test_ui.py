# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details

from thrive.tests import tagged

from .test_sale_planning import TestSalePlanning
from thrive.addons.planning.tests.test_ui_common import TestUiCommon

@tagged('post_install', '-at_install')
class TestSalePlanningUi(TestSalePlanning, TestUiCommon):

    def test_01_ui_inherit(self):
        self.plannable_so.action_confirm()
        self.start_tour("/", 'sale_planning_test_tour', login='admin')
