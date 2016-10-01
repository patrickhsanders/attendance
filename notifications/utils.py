from .models import NotificationPreferences

def get_or_create_notification_preferences_for_student(student):

    try:
        preferences = NotificationPreferences.objects.get(student=student)
    except:
        preferences = NotificationPreferences.objects.create()
        student.email_preferences = preferences
        student.save()

    return student
