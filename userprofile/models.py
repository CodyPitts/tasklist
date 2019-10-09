from django.db import models
from django.contrib.auth.models import User
from usergroup.models import UserGroup


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    groups = models.ManyToManyField(UserGroup, blank=True)

    def __str__(self):
        return self.user.username
