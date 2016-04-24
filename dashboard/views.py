from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User, Permission
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class GenericDashboard(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'generic_dashboard.html'

    def get(self, request):

        current_user = request.user

        return render(
            request,
            self.template_name,
            {'current_user': current_user })