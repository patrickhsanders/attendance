from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import RecruitDashboard, ListWithoutRecruit
from .views import CreateJob, EditJob, JobsList, DeleteJob
from .views import CreateTask, EditTask, TaskList, CompleteTask, DeleteTask
from .views import CreateResume
from .views import CreateLink
from .views import CreateNote


urlpatterns = [

  url(r'^$', login_required(RecruitDashboard.as_view()), name="recruit_dashboard"),
  url(r'^no-recruit/$', login_required(ListWithoutRecruit.as_view()), name="recruit_students_no_recruit"),

  url(r'^(?P<recruit_id>[\w\-]+)/job/create', login_required(CreateJob.as_view()), name="add_job"),
  url(r'^job/(?P<job_id>[\w\-]+)/edit', login_required(EditJob.as_view()), name="edit_job"),
  url(r'^job/(?P<job_id>[\w\-]+)/delete', login_required(DeleteJob.as_view()), name="delete_job"),
  url(r'^job/$', login_required(JobsList.as_view()), name="list_job"),

  url(r'^(?P<recruit_id>[\w\-]+)/task/create', login_required(CreateTask.as_view()), name="add_task"),
  url(r'^task/$', login_required(TaskList.as_view()), name="list_job"),
  url(r'^task/(?P<task_id>[\w\-]+)/edit', login_required(EditTask.as_view()), name="edit_task"),
  url(r'^task/(?P<task_id>[\w\-]+)/complete', login_required(CompleteTask.as_view()), name="complete_task"),
  url(r'^task/(?P<task_id>[\w\-]+)/delete', login_required(DeleteTask.as_view()), name="delete_task"),

  url(r'^(?P<recruit_id>[\w\-]+)/resume/create', login_required(CreateResume.as_view()), name="add_resume"),

  url(r'^(?P<recruit_id>[\w\-]+)/link/create', login_required(CreateLink.as_view()), name="add_link"),

  url(r'^(?P<recruit_id>[\w\-]+)/note/create', login_required(CreateNote.as_view()), name="add_note_to_recruit"),

]