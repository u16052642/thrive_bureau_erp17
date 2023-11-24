# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    def _get_appraisal_plan_starting_date(self):
        self.ensure_one()
        return self.first_contract_date or self.create_date
