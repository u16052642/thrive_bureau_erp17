# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
from unittest.mock import patch

import thrive.tests
from thrive.addons.pos_self_order.tests.self_order_common_test import SelfOrderCommonTest
# from thrive.addons.pos_online_payment.models.pos_payment_method import PosPaymentMethod


@thrive.tests.tagged("post_install", "-at_install")
class TestSelfOrderFrontendMobile(SelfOrderCommonTest):
    pass
