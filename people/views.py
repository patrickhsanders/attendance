from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from attendance.models import Register
from .models import Student, ContactInfo, EmergencyContact
from course.models import Course
from django.db.models import Q
from django.contrib.auth.models import User, Permission
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from .forms import TelephoneNumberForm, AddressForm
from .forms import EmergencyContactForm

from django.http import HttpResponseRedirect

from rest_framework import viewsets
from .serializers import ActiveStudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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

        open_registers = Register.objects.filter(checkout=None).order_by('student__first_name')
        students = Student.objects.all().filter(~Q(id__in=[register.student.id for register in open_registers]), active="true",course__full_time=True).order_by('first_name')

        return render(
            request,
            self.template_name,
            {'student_list': students, 'open_registers': open_registers, 'success': success})

class StudentsCurrentlySignedInPortlet(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'
    template_name = 'student_checkin_current_portlet.html'

    def get(self, request):
        open_registers = Register.objects.filter(checkout=None).order_by('student__first_name')

        return render(
            request,
            self.template_name,
            {'open_registers': open_registers})

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

class ActiveStudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Student.objects.filter(end_date__isnull=True, active=True)
    serializer_class = ActiveStudentSerializer

class ContactInfoEditView(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_contact_info.html"

    def get(self, request, student_id):
        telephone_form = TelephoneNumberForm(prefix='TelephoneForm')
        address_form = AddressForm(prefix='AddressForm')

        return render(request, self.template_name, {'telephone_form': telephone_form, 'address_form': address_form})

    def post(self, request, student_id):
        bound_telephone_form = TelephoneNumberForm(request.POST, prefix='TelephoneForm')
        bound_address_form = AddressForm(request.POST, prefix='AddressForm')

        if bound_telephone_form.is_valid() and bound_address_form.is_valid():
            student = get_object_or_404(Student, pk=student_id)

            telephone_number = bound_telephone_form.save()
            address = bound_address_form.save()

            contact_info = ContactInfo()
            contact_info.phone_number = telephone_number
            contact_info.address = address
            contact_info.save()
            student.directory_information = contact_info
            student.save()

            return HttpResponseRedirect('/student/' + student_id + "/emergency-contact-info/edit")
        else:
            return render(request, self.template_name, {'telephone_form': bound_telephone_form, 'address_form': bound_address_form})

class EmergencyContactEditView(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_emergency_contact_info.html"

    def get(self, request, student_id):
        emergency_contact_form = EmergencyContactForm(prefix="EmergencyContactForm")
        telephone_form = TelephoneNumberForm(prefix='TelephoneForm1')
        telephone_form1 = TelephoneNumberForm(prefix='TelephoneForm2')
        address_form = AddressForm(prefix='AddressForm')

        return render(request, self.template_name, {'telephone_form1': telephone_form,'telephone_form2': telephone_form1, 'address_form': address_form, 'emergency_contact_form': emergency_contact_form})

    def post(self, request, student_id):
        bound_emergency_contact_form = EmergencyContactForm(request.POST, prefix="EmergencyContactForm")
        bound_telephone_form = TelephoneNumberForm(request.POST, prefix='TelephoneForm1')
        bound_telephone_form1 = TelephoneNumberForm(request.POST, prefix='TelephoneForm2')
        bound_address_form = AddressForm(request.POST, prefix='AddressForm')

        if bound_telephone_form.is_valid() and bound_address_form.is_valid() and bound_telephone_form.is_valid():
            student = get_object_or_404(Student, pk=student_id)

            telephone_number = bound_telephone_form.save()

            emergency_contact = bound_emergency_contact_form.save(commit=False)

            address = bound_address_form.save()
            emergency_contact.address = address
            emergency_contact.save()

            emergency_contact.telephone_numbers.add(telephone_number)

            if bound_telephone_form1.is_valid() and bound_telephone_form1.cleaned_data['phone_number']:
                telephone_number1 = bound_telephone_form1.save()
                emergency_contact.telephone_numbers.add(telephone_number1)

            emergency_contact.save()
            student.emergency_contact = emergency_contact
            student.save()

            return HttpResponseRedirect('/admin/people/student')
        else:
            return render(request, self.template_name,
                          {'telephone_form1': bound_telephone_form, 'telephone_form2': bound_telephone_form1,
                           'address_form': bound_address_form, 'emergency_contact_form': bound_emergency_contact_form})
