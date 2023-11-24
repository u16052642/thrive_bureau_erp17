# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive import models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def unlink(self):
        """ This override will delete all the private articles linked to the deleted partners. """
        self.env['knowledge.article.member'].sudo().search(
            [('partner_id', 'in', self.ids), ('article_id.category', '=', 'private')]
        ).article_id.unlink()
        return super(Partner, self).unlink()
