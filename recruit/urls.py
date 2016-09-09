from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CreateJob, EditJob, JobsList, DeleteJob
from .views import CreateTask, EditTask, TaskList
from .views import CreateResume


urlpatterns = [
  url(r'^(?P<recruit_id>[\w\-]+)/job/create', login_required(CreateJob.as_view()), name="add_job"),
  url(r'^job/(?P<job_id>[\w\-]+)/edit', login_required(EditJob.as_view()), name="edit_job"),
  url(r'^job/(?P<job_id>[\w\-]+)/delete', login_required(DeleteJob.as_view()), name="delete_job"),
  url(r'^job/$', login_required(JobsList.as_view()), name="list_job"),

  url(r'^(?P<recruit_id>[\w\-]+)/task/create', login_required(CreateTask.as_view()), name="add_task"),
  url(r'^task/(?P<task_id>[\w\-]+)/edit', login_required(EditTask.as_view()), name="edit_task"),
  url(r'^task/$', login_required(TaskList.as_view()), name="list_job"),

  url(r'^(?P<recruit_id>[\w\-]+)/resume/create', login_required(CreateResume.as_view()), name="add_resume"),

]