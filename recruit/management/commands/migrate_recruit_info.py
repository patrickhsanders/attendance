from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from recruit.models import Recruit
from people.models import Student
from note.models import Note


class Command(BaseCommand):
    help = "Closes all open registers and flags them as having failed to checkout"

    def handle(self, *args, **options):


        teddy = User.objects.get(username="patrick")

        all_students = Student.objects.all()
        for student in all_students:
            recruit = Recruit.objects.create()
            student.recruit = recruit
            recruit.save()
            student.save()

            if student.active == True:
                recruit.wants_help_looking_for_work = True
                recruit.save()

            if student.job_search_status != None:
                note = Note.objects.create(text=student.job_search_status, author=teddy)
                note.save()
                recruit.notes.add(note)
                recruit.save()
                self.stdout.write(self.style.SUCCESS("Added recruit to " + student.first_name + " with note"))
            else:
                self.stdout.write(self.style.SUCCESS("Added recruit to " + student.first_name))

