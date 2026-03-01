# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    daily_target = models.IntegerField()

    def __str__(self):
        return self.skill_name
