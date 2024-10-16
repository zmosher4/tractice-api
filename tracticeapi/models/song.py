from django.db import models
from .artist import Artist


class Song(models.Model):
    title = models.CharField(max_length=25)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    description = models.CharField(max_length=255)
