# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import api, models


class Onboarding(models.Model):
    _inherit = 'onboarding.onboarding'

    @api.model
    def action_close_panel_website_sale_dashboard(self):
        self.action_close_panel('website_sale_dashboard.onboarding_onboarding_website_sale_dashboard')
