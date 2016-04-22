from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Place


# Create your views here.

class PlacesChart(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    def get(self, request):

        return render(
            request,
            self.template_name,
            {'student_list': students_for_test, 'current_user_email':current_user_email, 'instructors':instructors})