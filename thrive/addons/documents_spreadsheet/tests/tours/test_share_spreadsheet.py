# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from ..common import SpreadsheetTestCommon

from thrive.tests import tagged
from thrive.tests.common import HttpCase


@tagged("post_install", "-at_install")
class TestSpreadsheetShareTour(SpreadsheetTestCommon, HttpCase):
    def test_open_public_spreadsheet(self):
        """check the public spreadsheet page can be opened without error"""
        spreadsheet = self.create_spreadsheet()
        share = self.share_spreadsheet(spreadsheet)
        # web_tour is not part of the public spreadsheet assets bundle.
        # We can't use the start_tour helper method.
        self.browser_js(
            "/document/share/%s/%s" % (share.id, share.access_token),
            "console.log('test successful');",
            ready="thrive.isReady",
        )
