from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from projects.models import StudentProject
from projects.models import Project

from finance.forms import StudentTuitionForm

from course.models import Course
from note.forms import NoteForm
from attendance.models import Register, ExcusedAbsence

from .models import Student, ContactInfo, EmergencyContact
from .forms import TelephoneNumberForm, AddressForm, StudentForm, WorkLanguageExperienceForm
from .forms import EmergencyContactForm, StudentJobStatusNoteForm, EducationalExperienceForm, EducationalInformationForm
from .serializers import ActiveStudentSerializer

# Create your views here.


class StudentList(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(
            request,
            'student_list.html',
            {'student_list': Student.people.active()})

    def test_func(self):
        return self.request.user


class StudentCheckin(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'

    template_name = 'student_checkin_list.html'

    def get(self, request, success):

        open_registers = Register.objects.filter(checkout=None).order_by('student__first_name')
        students = Student.people.active().fulltime().filter(
            ~Q(id__in=[register.student.id for register in open_registers]))

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

        students = Student.people.active().fulltime()
        current_user = request.user
        current_user_email = current_user.email

        return render(
            request,
            self.template_name,
            {'student_list': students, 'current_user_email': current_user_email})


class StudentTestEmailList(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'

    template_name = 'student_test_email_list.html'

    def get(self, request):

        students = Student.people.active().exclude(current_project=None)

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
            {'student_list': students_for_test, 'current_user_email': current_user_email, 'instructors': instructors})


class StudentListPortlet(PermissionRequiredMixin, ListView):
    template_name = "student_list_portlet.html"
    permission_required = 'people.add_student'
    model = Student
    default_queryset = 'active'

    def get_queryset(self):

        filter = self.request.GET.get('filter') if self.request.GET.get('filter') is not None else self.default_queryset

        if filter == 'active':
            return Student.people.active()
        elif filter == 'inactive':
            return Student.people.inactive()
        elif filter == 'ios':
            return Student.people.active().ios()
        elif filter == 'android':
            return Student.people.active().android()
        elif filter == 'swift':
            return Student.people.swift()
        elif filter == 'algos':
            return Student.people.algos()
        elif filter == 'hackathon':
            return Student.people.hackathon()
        else:
            return Student.people.all()


class StudentListStartingSoonPortlet(PermissionRequiredMixin, ListView):
    template_name = "student_list_starting_soon.html"
    permission_required = 'people.add_student'
    model = Student

    def get_queryset(self):
        return Student.objects.filter(active=False, start_date__gte=timezone.now()).order_by('start_date')

class ActiveStudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Student.people.active().filter(end_date__isnull=True)
    serializer_class = ActiveStudentSerializer


class EditStudentJobStatus(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_job_status_edit.html'

    def get(self, request, student_id):

        form = None

        try:
            student = Student.objects.get(pk=student_id)
            form = StudentJobStatusNoteForm(initial={'job_search_status': student.job_search_status})
        except ObjectDoesNotExist:
            pass

        return render(request, self.template_name, {'form': form})

    def post(self, request, student_id):

        bound_form = StudentJobStatusNoteForm(request.POST)

        if bound_form.is_valid():
            student = get_object_or_404(Student, pk=student_id)
            student.job_search_status = bound_form.cleaned_data['job_search_status']
            student.save()

            return HttpResponseRedirect('/student/list/job-status/')
        else:
            return render(request, self.template_name, {'form': bound_form})


class StudentJobStatusList(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_job_status_list.html'

    def get(self, request):

        students_without_status = Student.objects.filter(job_search_status__isnull=True)
        students_with_status = Student.objects.filter(job_search_status__isnull=False)

        return render(request, self.template_name, {'students_with_status': students_with_status,
                                                    'students_without_status': students_without_status})


class DeleteStudentJobStatus(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_job_status_delete_confirmation.html'

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        return render(request, self.template_name, {'student': student})

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        student.job_search_status = None
        student.save()

        return HttpResponseRedirect('/student/list/job-status/')


class AttendanceDisplay():
    def __init__(self, day, status):
        self.day = day
        self.status = status


class StudentDetailView(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_detail.html'

    @staticmethod
    def datetime_range(start, end, delta):
        date_list = []
        current = start
        if not isinstance(delta, timedelta):
            delta = timedelta(**delta)

        while current <= end:
            if current.weekday() != 5 and current.weekday() != 6:
                date_list.append(current)
            current += delta

        return date_list

    def get(self, request, student_id):

        student = get_object_or_404(Student, pk=student_id)
        projects = StudentProject.objects.filter(student=student).order_by('-date_started')
        note_form = NoteForm()

        registers = Register.objects.filter(student=student)
        excused_absence = ExcusedAbsence.objects.filter(student=student)

        end_date = timezone.now().date() if student.end_date is None else student.end_date
        date_list = self.datetime_range(student.start_date, end_date, {'days': 1})
        attendance = []

        for date in date_list:
            register_result = registers.filter(checkin__day=date.day,
                                               checkin__month=date.month,
                                               checkin__year=date.year)

            if not register_result:
                excused_absence_result = excused_absence.filter(start_date__lte=date, end_date__gte=date)
                if not excused_absence_result:
                    status = "Absent"
                else:
                    status = "Absent - Excused"
            else:
                status = "Present"

            obj_ = AttendanceDisplay(date, status)
            attendance.append(obj_)

        remaining_to_pay = 0.0
        total_paid = 0.0

        if student.tuition is not None:
            for payment in student.tuition.payments.all():
                if payment.completed == True:
                    total_paid += payment.amount
                elif payment.completed == False:
                    remaining_to_pay += payment.amount

            if total_paid == 0:
                remaining_to_pay = student.tuition.tuition_total

        excused_absences = ExcusedAbsence.objects.filter(student=student)

        relationship_dictionary = dict(EmergencyContact.RELATIONSHIP_CHOICES)
        if student.emergency_contact is not None:
            full_emergency_contact_relationship = relationship_dictionary.get(student.emergency_contact.relationship)
        else:
            full_emergency_contact_relationship = None

        return render(request, self.template_name, {'student': student,
                                                    'projects':projects,
                                                    'emergency_contact_relationship':full_emergency_contact_relationship,
                                                    'note_form' : note_form,
                                                    'attendance': reversed(attendance),
                                                    'excused_absences': excused_absences,
                                                    'total_paid': total_paid,
                                                    'remaining_to_pay': remaining_to_pay, })


class AddNoteToStudent(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    default_redirect = '/'

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        bound_form = NoteForm(request.POST)
        if bound_form.is_valid():
            note = bound_form.save(commit=False)
            note.author = request.user
            note.save()
            student.notes.add(note)

        redirect = request.GET.get('next') if request.GET.get('next') is not None else self.default_redirect
        return HttpResponseRedirect(redirect)


class CreateStudent(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_start.html'

    def get(self, request):
        form = StudentForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        bound_form = StudentForm(request.POST)
        if bound_form.is_valid():
            student = bound_form.save()

            if student.start_date == timezone.now().date():
                student.active = True
                projects = Project.objects.filter(course=student.course)[:1]
                if projects.count() != 0:
                    student.current_project = projects[0]

            elif student.start_date < timezone.now().date():
                student.end_date = student.start_date

            student.save()

            default_redirect = '/student/' + str(student.pk) + "/contact-info/edit"
            redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect
            return HttpResponseRedirect(redirect)

        else:
            return render(request, self.template_name, {'form': bound_form})


class ContactInfoEditView(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_contact_info.html"

    def get(self, request, student_id):
        try:
            contact = ContactInfo.objects.get(student__pk=student_id)
            print(contact)
            telephone_form = TelephoneNumberForm(prefix='TelephoneForm', instance=contact.phone_number)
            address_form = AddressForm(prefix='AddressForm',instance=contact.address)
        except:
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

            default_redirect = '/student/' + str(student.pk) + "/education-info/edit"

            redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect

            return HttpResponseRedirect(redirect)
        else:
            return render(request, self.template_name,
                          {'telephone_form': bound_telephone_form, 'address_form': bound_address_form})


class EducationInformationView(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_educational_info.html"

    def get(self, request, student_id):
        education_information = EducationalInformationForm(prefix="edu_info")
        degree_1 = EducationalExperienceForm(prefix="degree_1")
        degree_2 = EducationalExperienceForm(prefix="degree_2")

        return render(request, self.template_name, {'education_information': education_information,
                                                    'degree_1': degree_1,
                                                    'degree_2': degree_2 })

    def post(self, request, student_id):
        education_information_form = EducationalInformationForm(request.POST, prefix="edu_info")
        degree_1_form = EducationalExperienceForm(request.POST, prefix="degree_1")
        degree_2_form = EducationalExperienceForm(request.POST, prefix="degree_2")

        if education_information_form.is_valid() and degree_1_form.is_valid():
            student = get_object_or_404(Student, pk=student_id)
            education_information = education_information_form.save()
            degree_1 = degree_1_form.save()
            education_information.education.add(degree_1)

            if degree_2_form.is_valid():
                degree_2 = degree_2_form.save()
                education_information.education.add(degree_2)

            education_information.save()
            student.education = education_information
            student.save()

            default_redirect = '/student/' + str(student.pk) + "/additional-info/edit"
            redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect

            return HttpResponseRedirect(redirect)

        else:
            return render(request, self.template_name, {'education_information': education_information_form,
                                                        'degree_1': degree_1_form,
                                                        'degree_2': degree_2_form})


class EmergencyContactEditView(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_emergency_contact_info.html"

    def get(self, request, student_id):
        emergency_contact_form = EmergencyContactForm(prefix="EmergencyContactForm")
        telephone_form = TelephoneNumberForm(prefix='TelephoneForm1')
        telephone_form1 = TelephoneNumberForm(prefix='TelephoneForm2')

        return render(request, self.template_name,
                      {'telephone_form1': telephone_form, 'telephone_form2': telephone_form1,
                       'emergency_contact_form': emergency_contact_form})

    def post(self, request, student_id):
        bound_emergency_contact_form = EmergencyContactForm(request.POST, prefix="EmergencyContactForm")
        bound_telephone_form = TelephoneNumberForm(request.POST, prefix='TelephoneForm1')
        bound_telephone_form1 = TelephoneNumberForm(request.POST, prefix='TelephoneForm2')

        if bound_telephone_form.is_valid() and bound_emergency_contact_form.is_valid():
            student = get_object_or_404(Student, pk=student_id)

            telephone_number = bound_telephone_form.save()

            emergency_contact = bound_emergency_contact_form.save()
            emergency_contact.telephone_numbers.add(telephone_number)

            if bound_telephone_form1.is_valid() and bound_telephone_form1.cleaned_data['phone_number']:
                telephone_number1 = bound_telephone_form1.save()
                emergency_contact.telephone_numbers.add(telephone_number1)

            emergency_contact.save()
            student.emergency_contact = emergency_contact
            student.save()

            default_redirect = '/student/' + str(student.pk) + "/education-info/edit"
            redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect

            return HttpResponseRedirect(redirect)
        else:
            return render(request, self.template_name,
                          {'telephone_form1': bound_telephone_form, 'telephone_form2': bound_telephone_form1,
                           'emergency_contact_form': bound_emergency_contact_form})


class CreateAdditonalData(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = 'student_additional_information.html'

    def get(self, request, student_id):
        form = WorkLanguageExperienceForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        bound_form = WorkLanguageExperienceForm(request.POST, instance=student)
        if bound_form.is_valid():
            bound_form.save()

            default_redirect = '/student/' + str(student.pk) + "/confirm"
            redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect
            return HttpResponseRedirect(redirect)

        else:
            return render(request, self.template_name, {'form': bound_form })


class StudentContract(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_contract.html"

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        today = timezone.now().date()
        return render(request, self.template_name, {'student':student, 'today': today } )

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        student.contract_on_file = True
        student.save()

        default_redirect = '/student/' + str(student.pk)
        redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect
        return HttpResponseRedirect(redirect)


class StudentAddConfirmation(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_create_confirmation.html"

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        return render(request, self.template_name, {'student': student})


class StudentTuition(PermissionRequiredMixin, View):
    permission_required = 'finance.add_payment'
    template_name = "student_tuition.html"

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        tuition_form = StudentTuitionForm(prefix='TuitionForm')
        note_form = NoteForm(prefix='NoteForm')
        return render(request, self.template_name, {'student':student, 'form':tuition_form, 'note':note_form })

    def post(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)

        bound_tuition_form = StudentTuitionForm(request.POST, prefix='TuitionForm')
        bound_note_form = NoteForm(request.POST, prefix='NoteForm')

        if bound_tuition_form.is_valid():
            obj_ = bound_tuition_form.save()
            student.tuition = obj_
            student.save()

            print(bound_note_form)
            if bound_note_form.is_valid() and bound_note_form.data['NoteForm-text']:
                note = bound_note_form.save(commit=False)
                note.author = request.user
                note.save()
                obj_.notes.add(note)
                obj_.save()

            default_redirect = '/student/' + str(student.pk)
            redirect = request.GET.get('next') if request.GET.get('next') is not None else default_redirect
            return HttpResponseRedirect(redirect)

        else:
            return render(request, self.template_name, {'student': student, 'form': bound_tuition_form, 'note': bound_note_form})


class CompletionCalendar(PermissionRequiredMixin, View):
    permission_required = 'people.add_student'
    template_name = "student_completion_calendar.html"

    def get(self, request, student_id):
        student = get_object_or_404(Student, pk=student_id)
        finished_projects = StudentProject.objects.filter(student=student)

        current_student_project = StudentProject.objects.filter(student=student, project__weight__lt=1000).order_by('-project__weight')[:1][0]
        remaining_projects = Project.objects.filter(course=student.course,
                                                    weight__gt=current_student_project.project.weight,
                                                    deprecated=False,
                                                    weight__lt=1000).order_by('weight')

        if student.current_project.estimated_completion_days < current_student_project.project.estimated_completion_days:
            pass

        day = timezone.now().date()

        if current_student_project.derived_days < current_student_project.project.estimated_completion_days:
            day += timedelta(days=current_student_project.project.estimated_completion_days - current_student_project.derived_days)

        projects = []

        for project in remaining_projects:
            student_project = StudentProject()
            student_project.project = project
            student_project.date_started = day
            projects.append(student_project)

            for x in range(0, project.estimated_completion_days):
                day += timedelta(days=1)

        return render(request, self.template_name, {'student': student,
                                                    # 'finished_projects': finished_projects,
                                                    'remaining_projects': projects,
                                                    'final_day': day})
