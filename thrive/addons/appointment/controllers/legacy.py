
from thrive import http
from thrive.http import request
from thrive.addons.base.models.ir_qweb import keep_query

class AppointmentLegacy(http.Controller):
    """
        Retro compatibilyt layer for legacy endpoint
    """

    @http.route(['/calendar/<model("appointment.type"):appointment_type>/appointment'],
                type='http', auth='public', website=True, sitemap=True)
    def calendar_appointment(self, appointment_type, filter_staff_user_ids=None, timezone=None, failed=False, **kwargs):
        return request.redirect('/calendar/%s?%s' % (appointment_type.id, keep_query('*')))
