from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class university(models.Model):
    university_name = models.CharField(max_length=100)
    def __str__(self):
        return self.university_name

class department(models.Model):
    university = models.ForeignKey(university, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def university_name(self):
        return self.university.university_name
    def __str__(self):
        return self.name

class subject(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    def department_name(self):
        return self.department.name
    def __str__(self):
        return self.subject

class questionanswer(models.Model):
    ques= models.TextField()
    answer=models.TextField()
    username=models.CharField(max_length=100)
    university_select = models.ForeignKey(university, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    semester=models.CharField(max_length=25)
    year=models.IntegerField()
    show=models.BooleanField(default=False)
    timesAsked=models.CharField(max_length=2,blank=True,null=True)
    comment=models.CharField(max_length=500,null=True)
    important=models.BooleanField(default=False)
    def __str__(self):
        return self.ques[:30]

class feedback_m(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.message[13:30]

class Profile(models.Model):
    username = models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    def __str__(self):
        return self.username

