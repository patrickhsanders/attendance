from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from attendance.models import Register
from .models import Student
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth.models import User, Permission

# Create your views here.

class StudentList(View):

    template_name = 'blog/post_list.html'

    def get(self, request, parent_template=None):
        return render(
            request,
            'student_list.html',
            {'student_list':Student.objects.all().filter(active="true").order_by('first_name') })

class StudentCheckin(View):

    template_name = 'student_checkin_list.html'

    def get(self, request, parent_template=None):

        open_registers = Register.objects.filter(checkout=None).order_by('student__first_name')
        students = Student.objects.all().filter(~Q(id__in=[register.student.id for register in open_registers]), active="true",course__full_time=True).order_by('first_name')

        return render(
            request,
            self.template_name,
            {'student_list': students, 'open_registers': open_registers})

class StudentEmailList(View):

    template_name = 'student_email_list.html'

    def get(self, request):

        students = Student.objects.filter(active=True).order_by('first_name')
        current_user = request.user
        current_user_email = current_user.email

        return render(
            request,
            self.template_name,
            {'student_list': students, 'current_user_email':current_user_email})

class StudentTestEmailList(View):

    template_name = 'student_test_email_list.html'

    def get(self, request):

        students = Student.objects.filter(active=True).order_by('first_name')
        current_user = request.user
        current_user_email = current_user.email

        instructors = User.objects.filter(groups__name="Instructors").exclude(username__iexact=current_user.username)

        return render(
            request,
            self.template_name,
            {'student_list': students, 'current_user_email':current_user_email, 'instructors':instructors})