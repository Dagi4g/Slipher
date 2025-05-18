from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Subtopics, SubTopicMemory 

@receiver(post_save, sender=Subtopics)
def create_topic_review(sender, instance, created, **kwargs):
    if created and instance.review:
        sub = SubTopicMemory.objects.create(
                subtopic=instance,
        )
        sub.first_review_date()

