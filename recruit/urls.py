from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .forms import RecruitForm, ResumeForm, TaskForm, JobForm, CompanyForm
from .views import CreateJob

urlpatterns = [
 url(r'^(?P<recruit_id>[\w\-]+)/job/create', login_required(CreateJob.as_view()), name="checkin"),

]