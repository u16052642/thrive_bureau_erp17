# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from markupsafe import Markup
from thrive import models, _


class MailBot(models.AbstractModel):
    _inherit = 'mail.bot'

    def _get_answer(self, record, body, values, command):
        thrivebot_state = self.env.user.thrivebot_state
        if self._is_bot_in_private_channel(record):
            if thrivebot_state == "onboarding_attachement" and values.get("attachment_ids"):
                self.env.user.thrivebot_failed = False
                self.env.user.thrivebot_state = "onboarding_canned"
                return Markup(_("That's me! 🎉<br/>Try typing %s to use canned responses.", "<span class=\"o_thrivebot_command\">:</span>"))
            elif thrivebot_state == "onboarding_canned" and values.get("canned_response_ids"):
                self.env.user.thrivebot_failed = False
                self.env.user.thrivebot_state = "idle"
                return Markup(_("Good, you can customize canned responses in the live chat application.<br/><br/><b>It's the end of this overview</b>, enjoy discovering Thrive!"))
            # repeat question if needed
            elif thrivebot_state == 'onboarding_canned' and not self._is_help_requested(body):
                self.env.user.thrivebot_failed = True
                return _("Not sure what you are doing. Please, type %s and wait for the propositions. Select one of them and press enter.",
                    Markup("<span class=\"o_thrivebot_command\">:</span>"))
        return super(MailBot, self)._get_answer(record, body, values, command)
