from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib import admin

from .models import Student
from attendance.models import Register
from django.utils import timezone
from django.core import validators
from .forms import RegisterForm
from projects.models import Project, StudentProject
from django.contrib.auth.mixins import PermissionRequiredMixin

class CloseRegister(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'

    def get(self, request, register_id):

        register_obj = Register.objects.filter(id=register_id)
        register_obj.update(checkout=timezone.now())

        current_register = register_obj[0]

        if current_register.current_curriculum_project != None:

            try:
                student_project = StudentProject.objects.get(student=current_register.student, project=current_register.current_curriculum_project)
                time_delta = current_register.checkout - current_register.checkin
                student_project.derived_hours += (time_delta.seconds / 60 / 60)
                student_project.save()

            except StudentProject.DoesNotExist:
                pass

        return redirect('checkin')


class CreateRegister(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'

    form_class = RegisterForm
    model = Register

    def get(self,request,student_id):

        student_obj = Student.objects.get(id=student_id)
        previous_register = Register.objects.filter(student=student_obj).order_by('-checkout')

        student_course = student_obj.course

        if previous_register:
            previous_register = previous_register[0]
            current_project_c = previous_register.current_curriculum_project
            form = RegisterForm(course=student_course, initial={'current_curriculum_project':current_project_c, 'student':student_obj})
        else:
            form = RegisterForm(course=student_course,initial={'student':student_obj})

        return render(request,'student_checkin_form.html',{'form': form, 'student':student_obj})

    def post(self, request, student_id):
        student_obj = Student.objects.get(id=student_id)
        current_project_id = request.POST['current_curriculum_project']
        if current_project_id != "":
            current_project = Project.objects.get(id=current_project_id)

            try:
                student_project = StudentProject.objects.get(student=student_obj, project=current_project)
                student_project.derived_days += 1
                student_project.save()
            except StudentProject.DoesNotExist:
                student_project = StudentProject(student=student_obj, project=current_project)
                student_project.save()

        else:
            current_project = None

        if (Register.objects.filter(student=student_obj, checkout=None).count() == 0):
            Register.objects.create(student=student_obj, current_curriculum_project=current_project)
            return redirect('checkin')
        else:
            # send back failure
            return redirect('checkin')