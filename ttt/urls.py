"""ttt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from people.views import StudentList
from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import include

from attendance import urls as attendance_urls
from people.views import StudentCheckin, StudentList, StudentEmailList, StudentTestEmailList, StudentListPortlet, StudentListStartingSoonPortlet
from django.views.generic.base import RedirectView
from dashboard.views import GenericDashboard

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/admin')),
    url(r'^admin/', admin.site.urls),

    url(r'^student/list$', login_required(StudentList.as_view())),
    url(r'^student/list/portlet$', login_required(StudentListPortlet.as_view())),
    url(r'^student/list/starting_soon/portlet$', login_required(StudentListStartingSoonPortlet.as_view())),

    url(r'^student/list/email/$', login_required(StudentEmailList.as_view())),
    url(r'^student/list/email/test/$', login_required(StudentTestEmailList.as_view())),

    url(r'^student/checkin/(?P<success>[\w\-]*)', login_required(StudentCheckin.as_view()), name="checkin"),

    url(r'^register/', include(attendance_urls)),

    url(r'^accounts/login/$', admin.site.login),

    url(r'^dashboard$', login_required(GenericDashboard.as_view())),

    # url(r'^api-auth/', include('rest_framework.urls',))
]