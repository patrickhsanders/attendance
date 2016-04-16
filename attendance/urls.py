from django.conf.urls import url
from .views import CreateRegister, CloseRegister
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    # url(r'^create/(?P<first_name>[\w\-]+)/(?P<last_name>[\w\-]+)/', CreateRegister.as_view(), name="register_create"),
    # url(r'^close/(?P<first_name>[\w\-]+)/(?P<last_name>[\w\-]+)/', CloseRegister.as_view(), name="register_close")
    url(r'^create/(?P<student_id>[\w\-]+)/', login_required(CreateRegister.as_view()), name="register_create"),
    url(r'^close/(?P<register_id>[\w\-]+)/', login_required(CloseRegister.as_view()), name="register_close")
]