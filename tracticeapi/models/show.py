from django.db import models
from django.contrib.auth.models import User
from .artist import Artist


class Show(models.Model):
    description = models.CharField(max_length=255)
    performance_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shows')
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='shows', null=True
    )
