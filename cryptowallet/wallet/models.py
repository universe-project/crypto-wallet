from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import time


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    address = models.CharField(
        max_length=100,
    )
    amount = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.user.username
