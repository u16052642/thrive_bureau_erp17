# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import api, models


class Onboarding(models.Model):
    _inherit = 'onboarding.onboarding'

    @api.model
    def action_close_panel_account_consolidation_dashboard(self):
        self.action_close_panel('account_consolidation.onboarding_onboarding_account_consolidation_dashboard')
