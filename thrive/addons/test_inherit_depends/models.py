# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class PublishedFoo(models.Model):
    _name = 'test_new_api.foo'
    _inherit = ['test_new_api.foo', 'test_inherit.mixin']
