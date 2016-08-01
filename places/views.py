from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Place


# Create your views here.
def process_tables_for_display_order(unordered_table):
    table_for_output = []
    for place in unordered_table[6:12]:
        table_for_output.append(place)

    for place in unordered_table[0:6:-1]:
        table_for_output.append(place)

    return table_for_output


class PlacesChart(PermissionRequiredMixin, View):
    permission_required = 'places.add_place'
    template_name = "places_chart.html"

    def get(self, request):

        west_table_group = process_tables_for_display_order(Place.objects.filter(frond="west").order_by('seat'))
        middle_table_group = process_tables_for_display_order(Place.objects.filter(frond="middle").order_by('seat'))
        east_table_group = process_tables_for_display_order(Place.objects.filter(frond="east").order_by('seat'))

        return render(
            request,
            self.template_name,
            {'east': east_table_group, 'middle':middle_table_group, 'west':west_table_group})



# from django.shortcuts import render
# from .models import Project
# from course.models import Course
#
# from django.views.generic import View
# from django.contrib.auth.mixins import PermissionRequiredMixin
#
# # Create your views here.
#
# class ProjectsListView(PermissionRequiredMixin, View):
#     permission_required = 'projects.add_project'
#     template_name = 'project_list_view.html'
#
#     def get(self, request):
#         android_course = Course.objects.get(name__iexact='Android Fulltime')
#         ios_course = Course.objects.get(name__iexact='iOS Fulltime')
#         ios_projects = Project.objects.filter(course=ios_course, weight__lt=1000)
#         android_projects = Project.objects.filter(course=android_course, weight__lt=1000)
#
#         return render(request, self.template_name, {'android_projects': android_projects, 'ios_projects':ios_projects})
