from django.db import models

from note.models import Note

class Company(models.Model):
    name = models.CharField(max_length=63)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=31, blank=True)


class Job(models.Model):
    title = models.CharField(max_length=63)
    salary = models.FloatField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    company = models.OneToOneField(Company, blank=True)


class Resume(models.Model):
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='resumes')


class Link(models.Model):

    LINK_TYPES = (('github', "GitHub"),
                  ('linkedin', "LinkedIn"),
                  ('website', "Personal Website"),
                  ('twitter', "Twitter"),
                  ('other', "Other"))

    type = models.CharField(max_length=15, choices=LINK_TYPES)
    url = models.URLField(max_length=200)


class Task(models.Model):
    TASK_CHOICES = (("resume", "Create resume"),
                    ("github", "Setup GitHub account and post important projects"),
                    ("website", "Setup personal portfolio website"),
                    ("linkedin", "Setup LinkedIn website"),
                    ("side project", "Finish side project and get in app store."),
                    ("personal app", "Create portfolio app"),
                    ("blog", "Create blog with posts about passion for app development, what you're learning, etc"),
                    ("hackathon", "Participate in Hackathon"),
                    ("other", "Other Task"))

    task = models.CharField(max_length=31)
    other = models.CharField(max_length=63, blank=True)
    date_to_finish_by = models.DateField()


class Recruit(models.Model):
    wants_help_looking_for_work = models.BooleanField(default=False)
    notes = models.ManyToManyField(Note, blank=True)
    jobs = models.ManyToManyField(Job, blank=True)
    links = models.ManyToManyField(Link, blank=True)
    resume = models.ManyToManyField(Resume, blank=True)
    tasks = models.ManyToManyField(Task, blank=True)