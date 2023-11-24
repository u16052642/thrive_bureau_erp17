# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class Partner(models.Model):
    _inherit = 'res.partner'
    _mailing_enabled = True
