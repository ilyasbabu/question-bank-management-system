from django.db import models

# Create your models here.
class university(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(university, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class subject(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class questionanswer(models.Model):
    ques= models.TextField()
    answer=models.TextField()
    university = models.ForeignKey(university, on_delete=models.CASCADE)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    year=models.IntegerField()
    show=models.BooleanField(default=False)