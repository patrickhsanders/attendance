from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User)
    text = models.TextField()

    soft_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:31]

