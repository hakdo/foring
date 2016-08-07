from django.db import models
from django.utils import timezone


# Create your models here.

class SimpleList(models.Model):
    shortname = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now())
    owner = models.CharField(max_length=200,default='dummy')
    contents = models.TextField()
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.shortname
