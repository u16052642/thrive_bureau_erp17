# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from . import models
from . import controllers


def _set_tax_on_work_in_out(env):
    env['product.product'].set_tax_on_work_in_out()
