# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from goals.models import Goal
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    date = models.DateField()
    topic = models.CharField(max_length=200)
    time_spent = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.topic