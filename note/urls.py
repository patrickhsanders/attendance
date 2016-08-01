from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import UpdateNote, DeleteNote #CreateNote,

urlpatterns = [
    # url(r'^create/$', CreateNote.as_view()),
    url(r'^(?P<note_id>[\w\-]+)/edit/$', login_required(UpdateNote.as_view())),
    url(r'^(?P<note_id>[\w\-]+)/delete/$', login_required(DeleteNote.as_view())),
    ]