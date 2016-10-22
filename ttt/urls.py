from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

from rest_framework import routers
from people.views import ActiveStudentViewSet

from attendance import urls as attendance_urls
from django.views.generic.base import RedirectView
from dashboard.views import GenericDashboard, AttendanceDashboard
from attendance.views import PresentStudentViewSet
from course.views import CourseViewSet
from projects.views import ProjectsListView
from places.views import PlacesChart

from people import urls as people_urls
from note import urls as note_urls
from finance import urls as finance_urls
from recruit import urls as recruit_urls
from notifications import urls as notification_urls

# REST Framework router setup.
router = routers.DefaultRouter()
router.register(r'student', ActiveStudentViewSet)
router.register(r'attendance', PresentStudentViewSet)
router.register(r'course',CourseViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/dashboard/')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),

    url(r'^note/', include(note_urls)),

    url(r'^student/$', login_required(GenericDashboard.as_view())),
    url(r'^student/', include(people_urls)),
    url(r'^finance/', include(finance_urls)),
    url(r'^recruit/', include(recruit_urls)),

    url(r'^project/$', login_required(ProjectsListView.as_view())),
    url(r'^place/$', login_required(PlacesChart.as_view())),

    url(r'^register/', include(attendance_urls)),

    url(r'^accounts/login/$', admin.site.login),

    url(r'^dashboard/$', login_required(GenericDashboard.as_view())),
    url(r'^dashboard/attendance/$', login_required(AttendanceDashboard.as_view())),

    url(r'^notifications/', include(notification_urls)),
]