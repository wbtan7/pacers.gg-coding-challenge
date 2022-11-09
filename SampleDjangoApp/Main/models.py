from django.db import models
from django.contrib.auth.models import AbstractUser

# Maintain a custom User class in case need to extend in the future 
class User(AbstractUser):
    pass

class ScoreLog(models.Model):

    score = models.FloatField(null=False, blank=False)
    score_2 = models.CharField(null=False, blank=False, max_length=10, default='EMPTY_BRO')

    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    # test_col = models.CharField(null=True, blank=True, max_length=2)