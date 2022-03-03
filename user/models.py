from django.db import models
from django.contrib.auth.models import User

class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.IntegerField()


class Profile(models.Model):
    username = models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    def __str__(self):
        return self.username