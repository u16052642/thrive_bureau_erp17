# -*- coding: utf-8 -*-
# Part of Thrive Bureau ERP. See LICENSE file for full copyright and licensing details.

from thrive.addons.appointment.controllers.calendar_view import AppointmentCalendarView
from thrive.http import request
from thrive.osv.expression import AND


class AppointmentHrRecruitmentCalendarView(AppointmentCalendarView):

    def _get_staff_user_appointment_invite_domain(self, appointment_type):
        domain = super()._get_staff_user_appointment_invite_domain(appointment_type)
        if 'default_applicant_id' in request.env.context:
            domain = AND([domain, [('applicant_id', '=', request.env.context['default_applicant_id'])]])
        return domain
