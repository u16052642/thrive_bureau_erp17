#-*- coding:utf-8 -*-
# Part of Thrive. See LICENSE file for full copyright and licensing details.

from . import controllers
from . import models
from . import wizard
from . import report

def _post_init_hook(env):
    env['res.company'].search([])._create_dashboard_notes()
