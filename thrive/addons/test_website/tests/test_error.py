import thrive.tests
from thrive.tools import mute_logger


@thrive.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(thrive.tests.HttpCase):

    @mute_logger('thrive.addons.http_routing.models.ir_http', 'thrive.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
