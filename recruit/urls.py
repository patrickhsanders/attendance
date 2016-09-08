from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .forms import RecruitForm, ResumeForm, TaskForm, JobForm, CompanyForm
from .views import CreateJob, EditJob, JobsList

urlpatterns = [
  url(r'^(?P<recruit_id>[\w\-]+)/job/create', login_required(CreateJob.as_view()), name="add_job"),
  url(r'^job/(?P<job_id>[\w\-]+)/edit', login_required(EditJob.as_view()), name="edit_job"),
  url(r'^job/$', login_required(JobsList.as_view()), name="list_job"),
]