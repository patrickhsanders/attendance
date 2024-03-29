from django.db import models
from django.core.urlresolvers import reverse

from note.models import Note
from .querysets import JobQueryset


class Company(models.Model):
    name = models.CharField(max_length=63)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=31, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=63)
    salary = models.FloatField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, blank=True, null=True)

    objects = JobQueryset.as_manager()

    def get_absolute_url(self):
        return reverse(
            'edit_job',
            kwargs={'job_id': self.pk})

    def get_delete_url(self):
        return reverse(
            'delete_job',
            kwargs={'job_id': self.pk})


class Resume(models.Model):
    date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='resumes')

    def get_delete_url(self):
        return reverse(
            'delete_resume',
            kwargs={'resume_id': self.pk})


class Link(models.Model):

    LINK_TYPES = (('github', "GitHub"),
                  ('linkedin', "LinkedIn"),
                  ('website', "Personal Website"),
                  ('twitter', "Twitter"),
                  ('blog', "Blog"),
                  ('app', "App Store Link"),
                  ('other', "Other"))

    type = models.CharField(max_length=15, choices=LINK_TYPES)
    other = models.CharField(max_length=31, blank=True)
    url = models.URLField(max_length=200)

    def get_delete_url(self):
        return reverse(
            'delete_link',
            kwargs={'link_id': self.pk})


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

    task = models.CharField(max_length=31, choices=TASK_CHOICES)
    other = models.CharField(max_length=63, blank=True)
    date_to_finish_by = models.DateField()
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(default=None, null=True)
    note = models.OneToOneField(Note, null=True)

    def get_absolute_url(self):
        return reverse(
            'edit_task',
            kwargs={'task_id': self.pk})

    def get_edit_url(self):
        return self.get_absolute_url()

    def get_complete_url(self):
        return reverse(
            'complete_task',
            kwargs={'task_id': self.pk})

    def get_delete_url(self):
        return reverse(
            'delete_task',
            kwargs={'task_id': self.pk})


class Recruit(models.Model):
    wants_help_looking_for_work = models.BooleanField(default=False)
    notes = models.ManyToManyField(Note, blank=True)
    jobs = models.ManyToManyField(Job, blank=True) # list, create
    links = models.ManyToManyField(Link, blank=True)
    resume = models.ManyToManyField(Resume, blank=True)
    tasks = models.ManyToManyField(Task, blank=True)

    def __str__(self):
        return "OBJ"

    def get_edit_url(self):
        return reverse(
            'recruit_edit',
            kwargs={'student_id': self.student.pk})

    def get_add_task_url(self):
        return reverse(
            'add_task',
            kwargs={'recruit_id': self.pk})

    def get_add_job_url(self):
        return reverse(
            'add_job',
            kwargs={'recruit_id': self.pk})

    def get_add_resume_url(self):
        return reverse(
            'add_resume',
            kwargs={'recruit_id': self.pk})

    def get_add_link_url(self):
        return reverse(
            'add_link',
            kwargs={'recruit_id': self.pk})

    def get_add_note_url(self):
        return reverse(
            'add_note_to_recruit',
            kwargs={'recruit_id': self.pk})
