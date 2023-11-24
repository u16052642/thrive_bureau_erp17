# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class CrmLead(models.Model):
    _inherit = 'crm.lead'
    _mailing_enabled = True
