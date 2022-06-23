from django.db import models

# Create your models here.
class Data(models.Model):
    subject_name = models.CharField(max_length = 100)
    topic_name = models.CharField(max_length = 100)
    hours_spent = models.IntegerField()
    mcq_solved = models.IntegerField()
    u_name = models.CharField(max_length=100,default="NULL")

    # def __str__(self):
    #     return self.title

class Subject(models.Model):
    subject_name = models.CharField(max_length = 100)
    u_name = models.CharField(max_length=100,default="NULL")

    # def __str__(self):
    #     return self.title
