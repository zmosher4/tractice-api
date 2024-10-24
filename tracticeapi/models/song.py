from django.db import models
from .artist import Artist


class Song(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
