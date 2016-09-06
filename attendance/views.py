from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from attendance.models import Register
from note.forms import NoteForm
from people.models import Student
from projects.models import Project, StudentProject

from .forms import ExcusedAbsenceForm, RegisterForm
from .models import DailyAttendance, DailyStatistics
from .serializers import PresentStudentSerializer


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

        return redirect('checkin',"success")


class CreateRegister(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'

    form_class = RegisterForm
    model = Register

    def get(self,request,student_id):

        student_obj = get_object_or_404(Student, id=student_id)
        student_course = student_obj.course

        if student_obj.current_project != None:
            form = RegisterForm(course=student_course, initial={'current_curriculum_project':student_obj.current_project, 'student':student_obj})
        else:
            form = RegisterForm(course=student_course,initial={'student':student_obj})

        return render(request,'student_checkin_form.html',{'form': form, 'student':student_obj})

    def post(self, request, student_id):
        student_obj = Student.objects.get(id=student_id)

        current_project_id = request.POST['current_curriculum_project']

        if current_project_id != "":
            current_project = Project.objects.get(id=current_project_id)
            if "Hackathon" not in current_project.name:
                student_obj.current_project = current_project

            student_obj.save()

            try:
                student_project = StudentProject.objects.get(student=student_obj, project=current_project)
                student_project.derived_days += 1
                student_project.save()
            except StudentProject.DoesNotExist:
                student_project = StudentProject(student=student_obj, project=current_project)
                student_project.save()

        else:
            current_project = None

        if (Register.objects.open().for_student(student_obj).count() == 0):
            Register.objects.create(student=student_obj, current_curriculum_project=current_project)
            return redirect('checkin', 'success')
        else:
            # send back failure
            return redirect('checkin')


class DailyAttendanceDetail(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'

    def get(self, request, daily_attendance_id):

        current_user = request.user

        daily_attendance = get_object_or_404(DailyAttendance, id=daily_attendance_id)
        # active_students = daily_attendance.active_students.order_by('first_name')
        active_students = Student.objects.filter(Q(id__in=[student.id for student in daily_attendance.active_students.all()])).order_by("first_name")

        dict = {}

        for student in active_students:
            if student in daily_attendance.present.all():
                dict[student] = True
            else:
                dict[student] = False

        return render(request,'daily_attendance_detail.html',{'current_user':current_user, 'active_students':active_students, 'dictionary':dict, 'title':daily_attendance.__str__()})

class DailyAttendanceListPortlet(PermissionRequiredMixin, ListView):
    permission_required = 'attendance.delete_register'

    template_name = "daily_attendance_detail_portlet.html"
    model = DailyAttendance

    def get_queryset(self):
        return DailyAttendance.objects.all().order_by('-date')

class DailyAttendanceList(PermissionRequiredMixin, ListView):
    permission_required = 'attendance.add_register'

    template_name = "daily_attendance_list.html"
    model = DailyAttendance

    def get_queryset(self):
        return DailyAttendance.objects.all().order_by('-date')

class DailyAttendanceStatisticsPortlet(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'
    template_name = "daily_attendance_stats_portlet.html"

    def get(self, request):
        previous_day_stats = DailyStatistics.objects.all().order_by("-date")[:1]
        previous_day_stats = previous_day_stats[0]

        return render(request,self.template_name,{'stats': previous_day_stats })

class DailyAttendanceDetailPortlet(PermissionRequiredMixin, ListView):
    permission_required = 'attendance.add_register'

    def get(self, request, daily_attendance_id):

        current_user = request.user

        daily_attendance = get_object_or_404(DailyAttendance, id=daily_attendance_id)
        # active_students = daily_attendance.active_students.order_by('first_name')
        active_students = Student.objects.filter(
            Q(id__in=[student.id for student in daily_attendance.active_students.all()])).order_by("first_name")

        dict = {}

        for student in active_students:
            if student in daily_attendance.present.all():
                dict[student] = True
            else:
                dict[student] = False

        return render(request, 'daily_attendance_portlet.html',
                      {'current_user': current_user, 'active_students': active_students, 'dictionary': dict,
                       'title': daily_attendance.__str__()})

class CreateExcusedAbsense(PermissionRequiredMixin, View):
    permission_required = 'attendance.add_register'
    template_name = 'create_excused_absence.html'
    default_redirect = '/'

    def get(self, request):
        absence_form = ExcusedAbsenceForm(prefix='absence_form')
        note_form = NoteForm(prefix='note_form')

        return render(request, self.template_name, {'absence_form': absence_form, 'note_form': note_form })

    def post(self, request):
        absence_form = ExcusedAbsenceForm(request.POST, prefix='absence_form')
        note_form = NoteForm(request.POST, prefix='note_form')


        if absence_form.is_valid():
            obj_ = absence_form.save()

            if note_form.is_valid():
                note = note_form.save(commit=False)
                if note.text != "":
                    note.author = request.user
                    note.save()
                    obj_.note = note
                    obj_.save()

        redirect = request.GET.get('next') if request.GET.get('next') != None else self.default_redirect
        return HttpResponseRedirect(redirect)


class PresentStudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = DailyAttendance.objects.filter().order_by('-date')[:1]
    serializer_class = PresentStudentSerializer