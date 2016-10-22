from django.conf.urls import url
from .views import UnsubscribeFromEmail

urlpatterns = [

    url(r'^unsubscribe/(?P<student_id>[\w\-]+)$',
        UnsubscribeFromEmail.as_view(),
        name="unsubscribe_from_email"),

]