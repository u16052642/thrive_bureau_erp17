# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.
from thrive import models
from thrive.tools import populate


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _populate_factories(self):
        res = super()._populate_factories()
        res += [("is_fsm", populate.randomize([True, False], [0.2, 0.8]))]
        return res
