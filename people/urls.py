from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import StudentCheckin, StudentList, StudentEmailList, StudentTestEmailList, StudentListPortlet, StudentListStartingSoonPortlet, StudentsCurrentlySignedInPortlet
from .views import ContactInfoEditView, EmergencyContactEditView
# from .views import ContactInfoViewPortlet


urlpatterns = [

    url(r'^list/$', login_required(StudentList.as_view())),
    url(r'^list/portlet/$', login_required(StudentListPortlet.as_view())),
    url(r'^list/starting_soon/portlet/$', login_required(StudentListStartingSoonPortlet.as_view())),

    url(r'^list/email/$', login_required(StudentEmailList.as_view())),
    url(r'^list/email/test/$', login_required(StudentTestEmailList.as_view())),

    url(r'^portlet/checked-in/$', login_required(StudentsCurrentlySignedInPortlet.as_view()), name="checked_in_portlet"),
    url(r'^checkin/(?P<success>[\w\-]*)', login_required(StudentCheckin.as_view()), name="checkin"),

    # url(r'^(?P<student_id>[\w\-]+)/contact-info/', login_required(ContactInfoView.as_view()), name="contact-info"),
    url(r'^(?P<student_id>[\w\-]+)/contact-info/edit/', login_required(ContactInfoEditView.as_view()), name="edit-contact-info"),
    url(r'^(?P<student_id>[\w\-]+)/emergency-contact-info/edit/', login_required(EmergencyContactEditView.as_view()), name="edit-emergency-contact-info")
]