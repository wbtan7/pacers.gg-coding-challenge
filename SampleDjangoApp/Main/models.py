from django.db import models
from django.contrib.auth.models import AbstractUser

# Maintain a custom User class in case need to extend in the future 
class User(AbstractUser):
    pass

class ScoreLog(models.Model):

    score = models.FloatField(null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)