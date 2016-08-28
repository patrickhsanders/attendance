from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import CreatePayment, EditPayment, PaymentsList, MonthPaymentList

urlpatterns = [
    url(r'^month/$', login_required(MonthPaymentList.as_view())),
    url(r'^(?P<tuition_id>[\w\-]+)/payment/add/$', login_required(CreatePayment.as_view())),
    url(r'^payment/(?P<payment_id>[\w\-]+)/edit/$', login_required(EditPayment.as_view())),
    url(r'^$', login_required(PaymentsList.as_view())),
]


