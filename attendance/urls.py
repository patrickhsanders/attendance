from django.conf.urls import url
from .views import CreateRegister, CloseRegister, DailyAttendanceDetail, DailyAttendanceListPortlet, DailyAttendanceStatisticsPortlet, DailyAttendanceDetailPortlet
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # url(r'^create/(?P<first_name>[\w\-]+)/(?P<last_name>[\w\-]+)/', CreateRegister.as_view(), name="register_create"),
    # url(r'^close/(?P<first_name>[\w\-]+)/(?P<last_name>[\w\-]+)/', CloseRegister.as_view(), name="register_close")
    url(r'^create/(?P<student_id>[\w\-]+)/', login_required(CreateRegister.as_view()), name="register_create"),
    url(r'^close/(?P<register_id>[\w\-]+)/', login_required(CloseRegister.as_view()), name="register_close"),
    url(r'^attendance/portlet/$', login_required(DailyAttendanceListPortlet.as_view()), name="daily_attendance_portlet"),
    url(r'^attendance/portlet/stats/$', login_required(DailyAttendanceStatisticsPortlet.as_view()), name="daily_attendance_statistics_portlet"),
    url(r'^attendance/(?P<daily_attendance_id>[\w\-]+)/$', login_required(DailyAttendanceDetail.as_view()), name="daily_attendance"),
    url(r'^attendance/(?P<daily_attendance_id>[\w\-]+)/portlet/$', login_required(DailyAttendanceDetailPortlet.as_view()), name="daily_attendance_detail_portlet"),

]