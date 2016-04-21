from django.core.management.base import BaseCommand, CommandError
from people.models import Student
from django.utils import timezone
from projects.models import Project

class Command(BaseCommand):
    help = "Closes all open registers and flags them as having failed to checkout"

    def handle(self, *args, **options):

        new_students_starting_today = Student.objects.filter(active=False, start_date=timezone.now(), course__isnull=False)

        for student in new_students_starting_today:
            first_project = Project.objects.filter(course=student.course).order_by('weight').first()
            student.current_project = first_project
            student.active = True
            student.save()

            self.stdout.write(self.style.SUCCESS(student.first_name + " " + student.last_name + " activated and started on project \"" + str(first_project) + "\""))
