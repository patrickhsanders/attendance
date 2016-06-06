from django.db import models
# from people.models import Student

class Job(models.Model):
    title = models.CharField(max_length=63)
    company = models.CharField(max_length=63)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    city = models.CharField(max_length=31, blank=True)


class WorkExperience(models.Model):
    jobs = models.ManyToManyField(Job)


class JobSearchSteps(models.Model):
    name = models.CharField(max_length=31)
    weight = models.IntegerField()


# class JobSearch
#     pass


class JobSearch(models.Model):
    pass

# class JobSearch(models.Model):
#     student = models.ForeignKey('people.Student')

    ## job hunt milestones -- convert to 121 relationship
    # CHARFIELD   status (NOT LOOKING, RESUME COMPLETE, MOCK INTERVIEWS, INTERVIEWING, COMPLETE)