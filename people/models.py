from __future__ import unicode_literals
from datetime import date
from django.db import models
from assets.models import Computer
from datetime import date
from course.models import Course


class Student(models.Model):
    COURSE_OPTIONS = (("ios-fulltime","iOS full-time intensive"),("android-fulltime", "android full-time intensive"),("swift","iOS part-time (Swift)"))
    LEVEL_OPTIONS = ((0, "Zero Beginner - no coding knowledge"),
    (1, "Beginner - has knowledge of computing concepts, "),
    (2, "Starter - some basic knowledge of programming"),
    (3, "Mover - knowledge of programming, academic or functional, frameworks"),
    (4, "Advanced - CS degree, or equivalent work experience"))
    
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    email = models.EmailField()
    #CHARFIELD   phone number 
    #URLS
    #URLFIELD  github link
    #URLFIELD  linkedin link

    #CHARFIELD  incoming level
    #BOOLEAN    has cs degree 
    
    start_date = models.DateField(default=date.today)
    # course = models.CharField(max_length=31, choices=COURSE_OPTIONS, default=COURSE_OPTIONS[0])
    course = models.ForeignKey(Course)
    current_project = models.ForeignKey('projects.Project', blank=True, null=True)
    
    # computer = models.ForeignKey(Computer, related_name='student_using', blank=True, null=True)
    uses_own_laptop = models.BooleanField(default=True)
    active = models.BooleanField(default = True)


    #jobs one to many (title(optional), start, end, current)
    #CHARFIELD   title (optional)
    #DATEFIELD   start date (optional)
    #DATEFIELD   end date (optional)
    #FOREIGNKEY  company
    #BOOLEAN     current
    
    
    #projects
    #CHARFIELD   name
    #URLFIELD    store link
    #BOOLEAN     complete
    
    
    #internship (same as job)
    #DATEFIELD   start date (optional)
    #DATEFIELD   end date (optional)
    #FOREIGNKEY  project
    
    
    #job search status (options)
    #CHARFIELD   status (NOT LOOKING, RESUME COMPLETE, MOCK INTERVIEWS, INTERVIEWING, COMPLETE)


    #Job hunt milestones
  

    def __str__(self):
        return self.first_name + " " + self.last_name
