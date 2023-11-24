# -*- coding: utf-8 -*-

from thrive import fields, models


class WebsiteTwitterTweet(models.Model):
    _inherit = 'website.twitter.tweet'
    _order = 'id desc'

    tweet_html = fields.Html()
    wall_ids = fields.Many2many('website.twitter.wall')
