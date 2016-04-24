from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from attendance.models import Register
from .models import Student
from course.models import Course
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.models import User, Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone

import time


# Create your views here.

class StudentList(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'blog/post_list.html'

    def get(self, request, parent_template=None):
        return render(
            request,
            'student_list.html',
            {'student_list':Student.objects.all().filter(active="true").order_by('first_name') })

    def test_func(self):
        return self.request.user

class StudentCheckin(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'

    template_name = 'student_checkin_list.html'

    def get(self, request, success):

        if success != "":
            print("YES")
        else:
            print("NOOOO")

        open_registers = Register.objects.filter(checkout=None).order_by('student__first_name')
        students = Student.objects.all().filter(~Q(id__in=[register.student.id for register in open_registers]), active="true",course__full_time=True).order_by('first_name')

        return render(
            request,
            self.template_name,
            {'student_list': students, 'open_registers': open_registers, 'success': success})

class StudentEmailList(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'student_email_list.html'

    def get(self, request):

        students = Student.objects.filter(active=True).order_by('first_name')
        current_user = request.user
        current_user_email = current_user.email

        return render(
            request,
            self.template_name,
            {'student_list': students, 'current_user_email':current_user_email})

class StudentTestEmailList(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'student_test_email_list.html'

    def get(self, request):

        students = Student.objects.filter(active=True).exclude(current_project=None).order_by('first_name')
        courses = Course.objects.filter(test_after_project__course__test_after_project_id__gte=0)

        students_for_test = []

        for student in students:
            test_after_project_with_weight = student.course.test_after_project.weight
            if student.current_project.weight > test_after_project_with_weight:
                students_for_test.append(student)

        current_user = request.user
        current_user_email = current_user.email

        instructors = User.objects.filter(groups__name="Instructors").exclude(username__iexact=current_user.username)

        return render(
            request,
            self.template_name,
            {'student_list': students_for_test, 'current_user_email':current_user_email, 'instructors':instructors})


class StudentListPortlet(PermissionRequiredMixin, ListView):
    template_name = "student_list_portlet.html"
    permission_required = 'people.add_student'
    model = Student

    def get_queryset(self):
        return Student.objects.filter(active=True).order_by('first_name')

class StudentListStartingSoonPortlet(PermissionRequiredMixin, ListView):
    template_name = "student_list_starting_soon.html"
    permission_required = 'people.add_student'
    model = Student

    def get_queryset(self):
        return Student.objects.filter(active=False, start_date__gte=timezone.now()).order_by('start_date')