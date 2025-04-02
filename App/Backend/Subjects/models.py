from datetime import date

from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Subjects(models.Model):
    subject_name = models.CharField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    
    def __str__(self):
        return self.subject_name

class Topics(models.Model):
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=500)

    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    
    def __str__(self):
        return self.topic_name

class Subtopics(models.Model):
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE)
    subtopic_name = models.CharField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    last_seen = models.DateTimeField(date.today().isoformat())

    def __str__(self):
        return self.subtopic_name

