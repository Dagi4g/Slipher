from django.db import models

class Subjects(models.Model):
    subject_name = models.CharField(max_length=500)
    rating = models.IntegerField(default=0)
    
    def __str__(self):
        return self.subject_name

class Topics(models.Model):
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=500)
    rating = models.IntegerField(default=3)
    
    def __str__(self):
        return self.topic_name
