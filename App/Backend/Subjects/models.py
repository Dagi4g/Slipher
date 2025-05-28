



from datetime import date

from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

from django.utils import timezone
    


class Subjects(models.Model):
    subject_name = models.CharField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    
    def __str__(self):
        return self.subject_name

class Topics(models.Model):
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,related_name="topic")
    topic_name = models.CharField(max_length=500)

    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    class Meta:
        unique_together = ("topic_name","subject")
    
    def __str__(self):
        return self.topic_name

class Subtopics(models.Model):
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE,related_name="subtopic")
    subtopic_name = models.CharField(max_length=500)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    last_seen = models.DateTimeField(default=timezone.now)
    review = models.BooleanField(default=True)
    class Meta:
        unique_together = ("subtopic_name","topic")

    def __str__(self):
        return self.subtopic_name

class SubtopicEntry(models.Model):
    subtopic = models.ForeignKey(Subtopics,on_delete=models.CASCADE,related_name="subtopicentry")
    text = models.TextField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.text

from datetime import date, timedelta

class SubTopicMemory(models.Model):
    subtopic = models.ForeignKey(Subtopics,on_delete=models.CASCADE)
    #building from subtopic up to subject without needing the anykind of id.

    #values used for calculation.
    memory_strength = models.FloatField(default=2.5)  # memory strength (like Anki's ease)
    interval = models.IntegerField(default=1)  # one day for next review days until next review
    next_review = models.DateField(default=timezone.now)
    revision_count = models.IntegerField(default=0)


    last_reviewed = models.DateField()# this value is from the form.
    
    def save(self,*args,**kwargs)-> None:
        # because in django the subtopics last seen date can't be used as
        # default we should instead set it manually.
        if not self.last_reviewed:
            # Doesn't have a default last reviewed set the subtopic last reviewd day.
            self.last_reviewed = self.subtopic.last_seen
            super().save(*args,**kwargs)

    @property
    def topic(self):
        return self.subtopic.topic
    
    @property
    def subject(self):
        return self.subtopic.topic.subject

    

    def calculate_interval(self):
        # in the interval calculation the subtopic has higher ranking and the topic has lower ranking.
        nonlinear_interval = (
                (self.subject.rating**1.5)*0.2+
                (self.topic.rating**1.2)*0.3+
                (self.subtopic.rating**1.1)*0.5)
                        # between 1(for all rating = 1)  and  7.06 (for rating = 5)
        return nonlinear_interval

    def calculate_next_review(self,base_interval: int,
                             ) -> int:
        """
        Calculates next review interval.
        - base_interval:is calculated using all the ratings.
        - rating_score: weighted score from subject/topic/subtopic ratings
        typical usage:
            self.calculate_next_review(base_interval)"""

        # Compound-like growth based on revision count.
        # the more the user reviewed a particular subtopic the more he/she is likely to remeber it so increase the interval.
        growth = self.memory_strength * (1 + 0.05 * self.revision_count)
        
        #- self.memory_strength: like Anki's ease factor.may vary according to different users.
        #- self.revision_count: how many times this subtopic has been reviewed. altered after each time of review.

        # Nonlinear boost from rating score (e.g., 0.5 to 1.5)

        self.interval = base_interval * growth 
        
        self.next_review = date.today() + timedelta(days=self.interval)
        # never forgate to save after changing the database.
        super().save()

        

    def first_review_date(self):
        """when called sets the next review day"""
        if self.pk and self.subtopic.review:
            # the subtopic doesn't exist.
            base_interval = self.calculate_interval()
            self.calculate_next_review(base_interval)
        else:
            pass 


    def update_memory(self, remembered: bool):
        if remembered:
            self.memory_strength += 0.1
            self.revision_count += 1 # another addtional revision.
            self.subtopic.rating = min(5,self.subtopic.rating + 0.3)
        else:
            self.interval = 1
            self.memory_strength = max(1.3, self.memory_strength - 0.1)
            #no matter the subtopic rating (even zero at first) it's minimum value will be 1.5.

            self.subtopic.rating = max(1.5, self.subtopic.rating - 0.3)

        

        self.subtopic.last_seen = date.today()
        interval = self.calculate_interval()
        self.calculate_next_review(interval)

        self.save()

    def __str__(self):
        return f"{self.subtopic.name} last reviewed on {self.last_reviewed}"

    def __repr__(self):
        return f"UserTopicMemory(subtopic={self.subtopic!r}, last_reviewed={self.last_reviewed!r},next_review={self.next_review})"

