from django.db import models
from usergroup.models import UserGroup
from userprofile.models import UserProfile


class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    users = models.ManyToManyField(UserProfile, blank=True)
    groups = models.ManyToManyField(UserGroup, blank=True)
    time_estimate = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title
