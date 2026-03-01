# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    partner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="partner_user")
    skills = models.CharField(max_length=200)
    streak_days = models.IntegerField(default=0)
    penalty_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
