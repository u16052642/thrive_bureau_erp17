# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

import json

from thrive.tests import HttpCase, tagged
from thrive.tools import mute_logger

@tagged('post_install', '-at_install')
class DomainTest(HttpCase):

    def test_domain_validate(self):
        self.authenticate("demo", "demo")

        with mute_logger('thrive.http'):
            resp = self.url_open(
                '/web/domain/validate',
                headers={'Content-Type': 'application/json'},
                data=json.dumps({'params': {'model':'i', 'domain':[]}}),
            )
        self.assertEqual(resp.json()['error']['data']['message'], "Invalid model: i")

        resp = self.url_open(
            '/web/domain/validate',
            headers={'Content-Type': 'application/json'},
            data=json.dumps({'params': {'model':'res.users', 'domain':[]}}),
        )
        self.assertEqual(resp.json()['result'], True)

        resp = self.url_open(
            '/web/domain/validate',
            headers={'Content-Type': 'application/json'},
            data=json.dumps({'params': {'model':'res.users', 'domain':[('name', 'ilike', 'ad')]}}),
        )
        self.assertEqual(resp.json()['result'], True)

        resp = self.url_open(
            '/web/domain/validate',
            headers={'Content-Type': 'application/json'},
            data=json.dumps({'params': {'model':'res.users', 'domain':[('hop')]}}),
        )
        self.assertEqual(resp.json()['result'], False)
