from django.db import models
from .song import Song
from .show import Show


class ShowSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='showsongs')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='showsongs')
