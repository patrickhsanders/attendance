from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import StudentCheckin, StudentList, StudentEmailList, StudentTestEmailList, StudentListPortlet, StudentListStartingSoonPortlet, StudentsCurrentlySignedInPortlet
from .views import ContactInfoEditView, EmergencyContactEditView
# from .views import ContactInfoViewPortlet
from .views import EditStudentJobStatus, StudentJobStatusList, DeleteStudentJobStatus, StudentDetailView, AddNoteToStudent, CreateStudent, StudentContract
from .views import EducationInformationView, CreateAdditonalData, StudentAddConfirmation, CompletionCalendar, StudentTuition
urlpatterns = [

    url(r'^create/$', login_required(CreateStudent.as_view())),

    url(r'^list/$', login_required(StudentList.as_view())),
    url(r'^list/portlet/$', login_required(StudentListPortlet.as_view())),
    url(r'^list/starting_soon/portlet/$', login_required(StudentListStartingSoonPortlet.as_view())),

    url(r'^list/email/$', login_required(StudentEmailList.as_view())),
    url(r'^list/email/test/$', login_required(StudentTestEmailList.as_view())),

    url(r'^portlet/checked-in/$', login_required(StudentsCurrentlySignedInPortlet.as_view()), name="checked_in_portlet"),
    url(r'^checkin/(?P<success>[\w\-]*)', login_required(StudentCheckin.as_view()), name="checkin"),

    url(r'^(?P<student_id>[\w\-]+)/$', login_required(StudentDetailView.as_view())),

    url(r'^(?P<student_id>[\w\-]+)/contact-info/edit/', login_required(ContactInfoEditView.as_view()), name="edit-contact-info"),
    url(r'^(?P<student_id>[\w\-]+)/emergency-contact-info/edit/', login_required(EmergencyContactEditView.as_view()), name="edit-emergency-contact-info"),
    url(r'^(?P<student_id>[\w\-]+)/education-info/edit/', login_required(EducationInformationView.as_view()),
        name="edit-emergency-contact-info"),
    url(r'^(?P<student_id>[\w\-]+)/additional-info/edit/', login_required(CreateAdditonalData.as_view()), name="edit-additional-info"),
    url(r'^(?P<student_id>[\w\-]+)/confirm/', login_required(StudentAddConfirmation.as_view()),
        name="student-add-confirmation"),

    url(r'^(?P<student_id>[\w\-]+)/job-status/edit/', login_required(EditStudentJobStatus.as_view())),
    url(r'^(?P<student_id>[\w\-]+)/job-status/delete/', login_required(DeleteStudentJobStatus.as_view())),

    url(r'(?P<student_id>[\w\-]+)/add-note', login_required(AddNoteToStudent.as_view())),
    url(r'(?P<student_id>[\w\-]+)/contract/$', login_required(StudentContract.as_view())),

    url(r'^list/job-status/$', login_required(StudentJobStatusList.as_view())),

    url(r'^(?P<student_id>[\w\-]+)/calendar/$', login_required(CompletionCalendar.as_view())),

    url(r'^(?P<student_id>[\w\-]+)/tuition/edit/$', login_required(StudentTuition.as_view())),

]