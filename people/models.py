from __future__ import unicode_literals
from django.db import models
from assets.models import Computer
from datetime import date
from django.utils import timezone
from course.models import Course
from localflavor.us.models import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField
from recruit.models import WorkExperience


class TelephoneNumber(models.Model):

    PHONE_NUMBER_TYPES = (('home', 'Home'),
                          ('work', 'Work'),
                          ('iphone', 'iPhone'),
                          ('mobile', 'Mobile'),
                          ('other', 'Other'))

    phone_number = PhoneNumberField(blank=True)
    type = models.CharField(max_length=10, choices=PHONE_NUMBER_TYPES, blank=True)

    def __str__(self):
        type_dict = dict(self.PHONE_NUMBER_TYPES)
        full_type = type_dict.get(self.type)
        return str(self.phone_number) + " " + full_type


class Address(models.Model):

    street_address = models.CharField(max_length=63)
    apt = models.CharField(max_length=31, blank=True)
    city = models.CharField(max_length=31)
    state = USStateField()
    zip = USZipCodeField()

    def __str__(self):
        return self.street_address + ", " + self.city


class Link(models.Model):

    LINK_TYPES = (('github', "GitHub"),
                  ('linkedin', "LinkedIn"),
                  ('website', "Personal Website"),
                  ('twitter', "Twitter"),
                  ('other', "Other"))

    type = models.CharField(max_length=15, choices=LINK_TYPES)
    url = models.URLField(max_length=200)


class EmergencyContact(models.Model):
    RELATIONSHIP_CHOICES = (('parent', 'Mother/Father'),
                            ('sibling', 'Brother/Sister'),
                            ('relative', 'Other relative'),
                            ('partner', 'Wife/Husband/Spouse'),
                            ('significant-other', 'Girlfriend/Boyfriend/Co-inhabitant'),
                            ('friend', 'Friend/Roommate'),
                            ('other', 'Other'))

    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    telephone_numbers = models.ManyToManyField(TelephoneNumber, blank=True)
    # address = models.ForeignKey(Address, blank=True, null=True)
    relationship = models.CharField(max_length=31, choices=RELATIONSHIP_CHOICES)

    def __str__(self):
        return self.first_name + " " + self.last_name


class EducationalExperience(models.Model):

    DEGREE_OPTIONS = (("hs","High School"),
                      ("aa","Associate's Degree"),
                      ("ba","Bachelor's Degree"),
                      ("ma","Master's Degree"),
                      ("mba","MBA"),
                      ("phd","Doctor of Philosophy"),
                      ("other","Other"))

    YEAR_CHOICES = [(x, x) for x in range(1985, timezone.now().year + 1)]
    YEAR_CHOICES.reverse()

    institution = models.CharField(max_length=63)
    field_of_study = models.CharField(max_length=63)
    degree = models.CharField(max_length=7, choices=DEGREE_OPTIONS)

    start_date = models.IntegerField(blank=True, choices=YEAR_CHOICES)
    end_date = models.IntegerField(blank=True, choices=YEAR_CHOICES)


class EducationalInformation(models.Model):
    LEVEL_OPTIONS = ((0, "Zero Beginner - no coding knowledge"),
                     (1, "Beginner - has knowledge of computing concepts, "),
                     (2, "Starter - some basic knowledge of programming"),
                     (3, "Mover - knowledge of programming, academic or functional, frameworks"),
                     (4, "Advanced - CS degree, or equivalent work experience"))

    education = models.ManyToManyField(EducationalExperience, blank=True)
    has_cs_degree = models.BooleanField(default=False)
    incoming_level = models.IntegerField(choices=LEVEL_OPTIONS, blank=True)


class ContactInfo(models.Model):
    phone_number = models.ForeignKey(TelephoneNumber, blank=True)
    address = models.ForeignKey(Address, blank=True)

    def __str__(self):
        return "Contact"


class Student(models.Model):
    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    email = models.EmailField()

    course = models.ForeignKey(Course)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(blank=True, null=True)
    current_project = models.ForeignKey('projects.Project', blank=True, null=True)

    uses_own_laptop = models.BooleanField(default=True)
    active = models.BooleanField(default = False)

    directory_information = models.OneToOneField("people.ContactInfo", blank=True, null=True)
    emergency_contact = models.OneToOneField("people.EmergencyContact", blank=True, null=True)
    links = models.ManyToManyField(Link, blank=True)
    education = models.OneToOneField(EducationalInformation, blank=True, null=True)
    work_experience = models.OneToOneField(WorkExperience, blank=True, null=True)

    class Meta:
        ordering = ('first_name',)

    def __str__(self):
        return self.first_name + " " + self.last_name


