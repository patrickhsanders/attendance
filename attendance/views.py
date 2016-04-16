from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib import admin

from .models import Student
from attendance.models import Register
from django.utils import timezone
from django.core import validators

class CreateRegister(View):

    def get(self,request,student_id):

        student_obj = Student.objects.get(id=student_id)
        previous_register = Register.objects.filter(student=student_obj).order_by('-checkout')
        if previous_register:
            previous_register = previous_register[0]

        return render(
            request,
            'student_checkin_detail.html',
            {'previous_register':previous_register, 'student':student_obj})

    def post(self, request, student_id):
        current_project = request.POST['current_project']
        student_obj = Student.objects.get(id=student_id)

        if (Register.objects.filter(student=student_obj, checkout=None).count() == 0):
            Register.objects.create(student=student_obj, current_project=current_project)
            # send back confirmation
            return redirect('checkin')
        else:
            # send back failure
            return redirect('checkin')

class CloseRegister(View):
    def get(self, request, register_id):

        register_obj = Register.objects.filter(id=register_id)
        register_obj.update(checkout=timezone.now())

        return redirect('checkin')