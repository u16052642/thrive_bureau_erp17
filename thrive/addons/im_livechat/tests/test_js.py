import thrive
from thrive.addons.web.tests.test_js import qunit_error_checker


@thrive.tests.tagged("post_install", "-at_install")
class ExternalTestSuite(thrive.tests.HttpCase):
    def test_external_livechat(self):
        # webclient external test suite
        self.browser_js("/web/tests/livechat?mod=web", "", "", login="admin", timeout=1800, error_checker=qunit_error_checker)
