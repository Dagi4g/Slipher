from datetime import date

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

class Subtopics(models.Model):
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE)
    subtopic_name = models.CharField(max_length=500)
    rating = models.IntegerField(default=3)
    last_seen = models.DateTimeField(date.today().isoformat())

    def __str__(self):
        return self.subtopic_name

