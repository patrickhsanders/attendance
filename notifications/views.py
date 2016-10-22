from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from people.models import Student
from .utils import get_or_create_notification_preferences_for_student, get_or_create_unsubscribe_token_for_student
# Create your views here.


class UnsubscribeFromEmail(View):
    template_name = 'unsubscribe_from_email.html'

    def get(self, request, student_id):

        student = get_object_or_404(Student, pk=student_id)

        return render(request, self.template_name, {'message':'hello', 'button':True})

    def post(self, request, student_id):

        student = get_object_or_404(Student, pk=student_id)
        student_token = get_or_create_unsubscribe_token_for_student(student).token
        given_token = request.GET['token']
        token_is_valid = True if given_token == student_token else False

        if token_is_valid:
            prefs = get_or_create_notification_preferences_for_student(student)
            prefs.receive_weekly_review = False
            prefs.save()
            message = "You have been unsubscribed"
        else:
            message = 'The provided unsubscribed token is invalid.'

        return render(request, self.template_name, {'message': message})
