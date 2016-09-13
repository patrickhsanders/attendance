from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import StudentCheckin, StudentList, StudentEmailList, StudentListPortlet, StudentListStartingSoonPortlet, StudentsCurrentlySignedInPortlet
from .views import ContactInfoEditView, EmergencyContactEditView
from .views import EditStudentJobStatus, StudentJobStatusList, DeleteStudentJobStatus, AddNoteToStudent, CreateStudent, StudentContract
from .views import StudentDetailViewGeneral, StudentDetailViewAttendance, StudentDetailViewCurriculum, StudentDetailViewFinance, StudentDetailViewRecruit
from .views import EducationInformationView, CreateAdditonalData, StudentAddConfirmation, CompletionCalendar, StudentTuition
from .views import ChangeStudentStatus
from recruit.views import CreateEditRecruit


urlpatterns = [

    url(r'^create/$',
        login_required(CreateStudent.as_view()),
        name="create_student"),

    # List display
    url(r'^list/$',
        login_required(StudentList.as_view()),
        name="student_list"),

    url(r'^list/portlet/$',
        login_required(StudentListPortlet.as_view()),
        name="student_list_portlet"),

    url(r'^list/starting_soon/portlet/$',
        login_required(StudentListStartingSoonPortlet.as_view()),
        name="student_starting_soon_portlet"),

    # Email list display
    url(r'^list/email/$',
        login_required(StudentEmailList.as_view()),
        name="student_list_email"),

    # Student checkin/checkout
    # TODO Should be moved to attendance module
    url(r'^portlet/checked-in/$',
        login_required(StudentsCurrentlySignedInPortlet.as_view()),
        name="checked_in_portlet"),

    url(r'^checkin/(?P<success>[\w\-]*)',
        login_required(StudentCheckin.as_view()),
        name="checkin"),

    # Student detail view

    url(r'^(?P<student_id>[\w\-]+)/attendance/$',
        login_required(StudentDetailViewAttendance.as_view()),
        name="student_detail_view_attendance"),

    url(r'^(?P<student_id>[\w\-]+)/curriculum/$',
        login_required(StudentDetailViewCurriculum.as_view()),
        name="student_detail_view_curriculum"),

    url(r'^(?P<student_id>[\w\-]+)/finance/$',
        login_required(StudentDetailViewFinance.as_view()),
        name="student_detail_view_finance"),

    url(r'^(?P<student_id>[\w\-]+)/recruit/$',
        login_required(StudentDetailViewRecruit.as_view()),
        name="student_detail_view_recruit"),

    url(r'^(?P<student_id>[\w\-]+)/$',
        login_required(StudentDetailViewGeneral.as_view()),
        name="student_detail_view"),

    # Student attribute edit
    url(r'^(?P<student_id>[\w\-]+)/contact-info/edit/',
        login_required(ContactInfoEditView.as_view()),
        name="edit-contact-info"),

    url(r'^(?P<student_id>[\w\-]+)/emergency-contact-info/edit/',
        login_required(EmergencyContactEditView.as_view()),
        name="edit-emergency-contact-info"),

    url(r'^(?P<student_id>[\w\-]+)/education-info/edit/',
        login_required(EducationInformationView.as_view()),
        name="edit-emergency-contact-info"),

    url(r'^(?P<student_id>[\w\-]+)/additional-info/edit/',
        login_required(CreateAdditonalData.as_view()),
        name="edit-additional-info"),

    url(r'^(?P<student_id>[\w\-]+)/confirm/',
        login_required(StudentAddConfirmation.as_view()),
        name="student-add-confirmation"),

    url(r'^(?P<student_id>[\w\-]+)/tuition/edit/$',
        login_required(StudentTuition.as_view()),
        name="edit_tuition"),

    url(r'^(?P<student_id>[\w\-]+)/status/edit/$',
        login_required(ChangeStudentStatus.as_view()),
        name="status_for_student"),

    url(r'(?P<student_id>[\w\-]+)/add-note',
        login_required(AddNoteToStudent.as_view()),
        name="add_note_to_student"),

    # Ideally would be in recruite app, but it makes more logical sense to be here based on the URL resolver
    url(r'(?P<student_id>[\w\-]+)/recruit/edit/?$',
        login_required(CreateEditRecruit.as_view()),
        name="recruit_edit"),

    # TODO Remove this view, it's been replaced
    url(r'^(?P<student_id>[\w\-]+)/job-status/edit/',
        login_required(EditStudentJobStatus.as_view()),
        name="edit_job_status"),

    # TODO Remove this view, it's been replaced
    url(r'^(?P<student_id>[\w\-]+)/job-status/delete/',
        login_required(DeleteStudentJobStatus.as_view()),
        name="delete_job_status"),

    url(r'(?P<student_id>[\w\-]+)/contract/$',
        login_required(StudentContract.as_view()),
        name="contract_detail_view"),

    # TODO Remove this view, it's been replaced
    url(r'^list/job-status/$',
        login_required(StudentJobStatusList.as_view()),
        name="job_status_list"),

    url(r'^(?P<student_id>[\w\-]+)/calendar/$',
        login_required(CompletionCalendar.as_view()),
        name="completion_calendar_display"),
]