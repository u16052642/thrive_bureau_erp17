# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive.http import request, route
from thrive.addons.mail.controllers.webclient import WebclientController
from thrive.addons.mail.models.discuss.mail_guest import add_guest_to_context


class WebClient(WebclientController):
    @route("/web/tests/livechat", type="http", auth="user")
    def test_external_livechat(self, **kwargs):
        return request.render("im_livechat.qunit_embed_suite", {
            "server_url": request.env["ir.config_parameter"].get_base_url(),
        })
