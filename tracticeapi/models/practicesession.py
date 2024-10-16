from django.db import models
from django.contrib.auth.models import User
from .show import Show


class PracticeSession(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="practice_sessions"
    )
    session_date = models.DateTimeField(null=True, blank=True)
    show = models.ForeignKey(
        Show, on_delete=models.CASCADE, related_name='practice_sessions'
    )
    notes = models.CharField(max_length=255)
