from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Subtopics, SubTopicMemory 

@receiver(post_save, sender=Subtopics)
def create_topic_review(sender, instance, created, **kwargs):
    """make calculating the review automatic and easy."""
    if instance.review:
        subtopic,_ = SubTopicMemory.objects.get_or_create(
                subtopic=instance,
        )#get or create returns two valuesin a tuple,the first one is the object and the second one is a boollian which indicates wether an object exists(True) or not (False).
        subtopic.first_review_date()

