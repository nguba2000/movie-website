from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Movie(models.Model):
    title = models.CharField('Movie Title', max_length=100)
    release_date = models.DateField()
    description = models.CharField('Synopsis', max_length = 500)

    def __str__(self):
        return(self.title)