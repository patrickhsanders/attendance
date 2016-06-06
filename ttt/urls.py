from django.conf.urls import url
from django.contrib import admin
# from people.views import StudentList
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import include

from rest_framework import routers
from people.views import ActiveStudentViewSet

from attendance import urls as attendance_urls
from people.views import StudentCheckin, StudentList, StudentEmailList, StudentTestEmailList, StudentListPortlet, StudentListStartingSoonPortlet, StudentsCurrentlySignedInPortlet
from django.views.generic.base import RedirectView
from dashboard.views import GenericDashboard, AttendanceDashboard
from people.views import ContactInfoEditView

from people import urls as people_urls

router = routers.DefaultRouter()
router.register(r'student', ActiveStudentViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/dashboard/')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),

    url(r'^student/', include(people_urls)),

    # url(r'^student/list$', login_required(StudentList.as_view())),
    # url(r'^student/list/portlet$', login_required(StudentListPortlet.as_view())),
    # url(r'^student/list/starting_soon/portlet$', login_required(StudentListStartingSoonPortlet.as_view())),
    #
    # url(r'^student/list/email/$', login_required(StudentEmailList.as_view())),
    # url(r'^student/list/email/test/$', login_required(StudentTestEmailList.as_view())),
    #
    # url(r'^student/portlet/checked-in/$', login_required(StudentsCurrentlySignedInPortlet.as_view()), name="checked_in_portlet"),
    # url(r'^student/checkin/(?P<success>[\w\-]*)', login_required(StudentCheckin.as_view()), name="checkin"),
    #
    #
    # url(r'^student/(?P<student_id>[\w\-]+)/contact-info/edit', login_required(ContactInfoEditView.as_view()), name="create-contact-info"),


    url(r'^register/', include(attendance_urls)),

    url(r'^accounts/login/$', admin.site.login),

    url(r'^dashboard/$', login_required(GenericDashboard.as_view())),
    url(r'^dashboard/attendance/$', login_required(AttendanceDashboard.as_view())),

    # url(r'^api-auth/', include('rest_framework.urls',))
]