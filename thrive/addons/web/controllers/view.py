# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive.exceptions import AccessError
from thrive.http import Controller, route, request
from thrive.tools.translate import _


class View(Controller):

    @route('/web/view/edit_custom', type='json', auth="user")
    def edit_custom(self, custom_id, arch):
        """
        Edit a custom view

        :param int custom_id: the id of the edited custom view
        :param str arch: the edited arch of the custom view
        :returns: dict with acknowledged operation (result set to True)
        """
        custom_view = request.env['ir.ui.view.custom'].sudo().browse(custom_id)
        if not custom_view.user_id == request.env.user:
            raise AccessError(_("Custom view %s does not belong to user %s", custom_id, self.env.user.login))
        custom_view.write({'arch': arch})
        return {'result': True}
