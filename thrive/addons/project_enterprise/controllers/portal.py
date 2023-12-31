# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import _
from thrive.addons.project.controllers.portal import ProjectCustomerPortal

class ProjectPortal(ProjectCustomerPortal):
    def _task_get_searchbar_sortings(self, milestones_allowed, project=False):
        values = super()._task_get_searchbar_sortings(milestones_allowed, project)
        values['planned_date_begin'] = {'label': _('Planned Date'), 'order': 'planned_date_begin asc', 'sequence': 7}
        return values
