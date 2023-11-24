# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import logging
import thrive.tests

_logger = logging.getLogger(__name__)


@thrive.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(thrive.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "thrive.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere('%s');" % menus[app_id]['xmlid'], "thrive.isReady === true", login="admin", timeout=1200)


@thrive.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(thrive.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_everywhere_as_demo(self):
        user_demo = self.env.ref("base.user_demo")
        menus = self.env['ir.ui.menu'].with_user(user_demo.id).load_menus(False)
        for app_id in menus['root']['children']:
            with self.subTest(app=menus[app_id]['name']):
                _logger.runbot('Testing %s', menus[app_id]['name'])
                self.browser_js("/web", "thrive.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere('%s');" % menus[app_id]['xmlid'], "thrive.isReady === true", login="demo", timeout=1200)

@thrive.tests.tagged('post_install', '-at_install')
class TestMenusAdminLight(thrive.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_admin(self):
        self.browser_js("/web", "thrive.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere(undefined, true);", "thrive.isReady === true", login="admin", timeout=120)

@thrive.tests.tagged('post_install', '-at_install')
class TestMenusDemoLight(thrive.tests.HttpCase):
    allow_end_on_form = True
    def test_01_click_apps_menus_as_demo(self):
        self.browser_js("/web", "thrive.loader.modules.get('@web/webclient/clickbot/clickbot_loader').startClickEverywhere(undefined, true);", "thrive.isReady === true", login="demo", timeout=120)
