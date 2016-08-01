from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from attendance.models import ExcusedAbsence
from django.utils import timezone

class GenericDashboard(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'student_dashboard.html'

    def get(self, request):

        current_user = request.user

        excused_absences = ExcusedAbsence.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())

        return render(
            request,
            self.template_name,
            {'current_user': current_user, 'title':"Dashboard", "excused_absences" : excused_absences })

class StudentDashboard(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_dashboard.html'

    def get(self, request):
        current_user = request.user
        excused_absences = ExcusedAbsence.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())

        return render(
            request,
            self.template_name,
            {'current_user': current_user, 'title': "Dashboard", "excused_absences": excused_absences})


class AttendanceDashboard(PermissionRequiredMixin, View):
    permission_required = 'attendance.change_register'

    template_name = 'attendance_dashboard.html'

    def get(self, request):

        current_user = request.user

        excused_absences = ExcusedAbsence.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())

        return render(
            request,
            self.template_name,
            {'current_user': current_user, 'title':"Dashboard", "excused_absences" : excused_absences })