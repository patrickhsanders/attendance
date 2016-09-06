from django.db import models
from people.models import Student
from projects.models import Project
from note.models import Note
from django.utils import timezone
from .querysets import RegisterQueryset


class Register(models.Model):
    student = models.ForeignKey(Student)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(blank=True, null=True)
    forgot_to_checkout = models.BooleanField(default=False)

    current_curriculum_project = models.ForeignKey(Project, blank=True, null=True)

    objects = RegisterQueryset.as_manager()

    def __str__(self):
        return self.student.first_name + " " + self.student.last_name + "(" + str(self.checkin.month) + "/" + str(self.checkin.day) + "/" + str(self.checkin.year) + " " + str(self.checkin.hour) + ":" + str(self.checkin.minute) + ")"


class ExcusedAbsence(models.Model):

    REASON_CHOICES = (('sick','Sick'),
                       ('vacation','Vacation / Traveling'),
                       ('working', 'Working'),
                       ('interviewing','Interviewing'),
                       ('other','Other'))

    student = models.ForeignKey(Student)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now, blank=True)
    reason = models.CharField(max_length=31, choices=REASON_CHOICES, blank=True, null=True)
    note = models.ForeignKey(Note, blank=True, null=True)

    def __str__(self):
        if self.start_date == self.end_date:
            return self.student.first_name + " " + self.student.last_name + " (" + self.start_date.strftime("%x") + "-" + self.end_date.strftime("%x") + ")"
        else:
            return self.student.first_name + " " + self.student.last_name + " (" + self.start_date.strftime(
                "%x") + ")"


class DailyAttendance(models.Model):
    date = models.DateField()
    active_students = models.ManyToManyField(Student, blank=True, related_name="active_students+")
    present = models.ManyToManyField(Student, blank=True, related_name="present+")
    absent = models.ManyToManyField(Student, blank=True, related_name="absent+")

    registers = models.ManyToManyField(Register, blank=True)

    def __str__(self):
        return "Attendance for " + str(self.date.month) + "/" + str(self.date.day) + "/" + str(self.date.year)


class DailyStatistics(models.Model):
    date = models.DateField()

    average_checkin = models.DateTimeField(blank=True, null=True)
    average_checkin_count = models.IntegerField(blank=True, null=True)

    average_hours_spent = models.FloatField(blank=True, null=True)
    average_hours_spent_count = models.IntegerField(blank=True, null=True)

    percent_students_present = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "Stats for " + str(self.date.month) + "/" + str(self.date.day) + "/" + str(self.date.year)
