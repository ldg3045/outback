from django.db import models
from django.contrib.auth.models import AbstractUser


"""이전 코드
class User(AbstractUser):


    nickname = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
"""


class User(AbstractUser):
    pass