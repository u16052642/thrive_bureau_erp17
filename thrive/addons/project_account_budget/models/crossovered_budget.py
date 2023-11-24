# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import api, models


class CrossoveredBudget(models.Model):
    _inherit = 'crossovered.budget'

    @api.model_create_multi
    def create(self, vals_list):
        budgets = super().create(vals_list)
        if len(budgets) == 1 and self.env.context.get('project_update'):  # Creation with Add Budget button in project update
            budgets.action_budget_confirm()
        return budgets
