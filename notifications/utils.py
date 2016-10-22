# from secrets import token_urlsafe # 3.6 + only
import uuid

from .models import NotificationPreferences, UnsubscribeToken

def get_or_create_notification_preferences_for_student(student):

    try:
        preferences = NotificationPreferences.objects.get(student=student)
    except:
        preferences = NotificationPreferences.objects.create()
        student.email_preferences = preferences
        student.save()

    return student.email_preferences


def get_or_create_unsubscribe_token_for_student(student):

    try:
        unsubscribe_token = UnsubscribeToken.objects.get(student=student)
    except:
        token = uuid.uuid4().hex[:30]
        unsubscribe_token = UnsubscribeToken.objects.create(student=student, token=token)

    return unsubscribe_token