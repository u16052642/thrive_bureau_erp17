# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import thrive.tests


@thrive.tests.tagged('post_install', '-at_install')
class TestUi(thrive.tests.HttpCase):

    def test_01_project_tour(self):
        self.start_tour("/web", 'project_tour', login="admin")
