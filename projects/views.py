from django.shortcuts import render
from .models import Project
from course.models import Course

from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class ProjectsListView(PermissionRequiredMixin, View):
    permission_required = 'projects.add_project'
    template_name = 'project_list_view.html'

    def get(self, request):
        android_course = Course.objects.get(name__iexact='Android Fulltime')
        ios_course = Course.objects.get(name__iexact='iOS Fulltime')
        ios_projects = Project.objects.filter(course=ios_course, weight__lt=1000, deprecated=False).order_by('weight')
        android_projects = Project.objects.filter(course=android_course, weight__lt=1000, deprecated=False).order_by('weight')

        return render(request, self.template_name, {'android_projects': android_projects, 'ios_projects':ios_projects})
