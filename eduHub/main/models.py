from django.db import models

# Create your models here.
class Data(models.Model):
    
    subject_name = models.CharField(max_length = 100)
    topic_name = models.CharField(max_length = 100)
    hours_spent = models.IntegerField()
    mcq_solved = models.IntegerField()

    def __str__(self):
        return self.title
