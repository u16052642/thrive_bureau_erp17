# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import base64

import thrive.tests
from thrive.tests.common import HOST
from thrive.tools import config

@thrive.tests.common.tagged('post_install', '-at_install')
class TestWebsiteGridLayout(thrive.tests.HttpCase):

    def test_01_replace_grid_image(self):
        IrAttachment = self.env['ir.attachment']
        base = "http://%s:%s" % (HOST, config['http_port'])
        req = self.opener.get(base + '/web/image/website.s_banner_default_image')
        IrAttachment.create({
            'public': True,
            'name': 's_banner_default_image.jpg',
            'type': 'binary',
            'res_model': 'ir_ui_view',
            'datas': base64.b64encode(req.content),
        })
        self.start_tour(self.env['website'].get_client_action_url('/'), 'website_replace_grid_image', login="admin")
