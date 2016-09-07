from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .forms import RecruitForm, ResumeForm, TaskForm, JobForm, CompanyForm

urlpatterns = [
 url(r'^checkin/(?P<success>[\w\-]*)', login_required(StudentCheckin.as_view()), name="checkin"),

]