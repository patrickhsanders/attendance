from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CreatePayment

urlpatterns = [
    url(r'^(?P<tuition_id>[\w\-]+)/payment/add/$', login_required(CreatePayment.as_view())),
]


