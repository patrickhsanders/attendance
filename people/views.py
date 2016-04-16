from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from attendance.models import Register
from .models import Student
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


# Create your views here.

class StudentList(View):

    template_name = 'blog/post_list.html'

    def get(self, request, parent_template=None):
        return render(
            request,
            'student_list.html',
            {'student_list':Student.objects.all().filter(active="true").order_by('first_name') })

class StudentCheckin(View):

    template_name = 'people/student_checkin_list.html'

    def get(self, request, parent_template=None):

        open_registers = Register.objects.filter(checkout=None).order_by('student__first_name')
        students = Student.objects.all().filter(~Q(id__in=[register.student.id for register in open_registers]), active="true",course__endswith="-fulltime").order_by('first_name')

        return render(
            request,
            'student_checkin_list.html',
            {'student_list': students, 'open_registers': open_registers})