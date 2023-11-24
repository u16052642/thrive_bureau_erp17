import thrive.tests
from thrive.tools import mute_logger


@thrive.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(thrive.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
