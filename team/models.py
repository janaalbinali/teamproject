from django.db import models

from django.contrib.auth.models import User



# Create your models here.


class Team(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    points = models.DecimalField(max_digits=120, decimal_places=2)

class Member(models.Model):
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    games_played = models.DecimalField(max_digits=120, decimal_places=2)