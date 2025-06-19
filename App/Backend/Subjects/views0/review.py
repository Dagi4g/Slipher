from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from  Subjects import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Prefetch

from datetime import date, timedelta

@method_decorator(csrf_exempt, name='dispatch')
class ShouldReviewView(View):
    def get(self,request):
        now = date.today()
        # Fetch subtopics that are due for review
        due_subtopics = models.SubTopicMemory.objects.filter(next_review__lte=now)

        if due_subtopics.exists():
            subtopic_list = []
            for subtopic in due_subtopics:
                subtopic_list.append({
                    "subtopic": subtopic.subtopic.subtopic_name, 
                    "topic": subtopic.subtopic.topic.topic_name, 
                    "subject": subtopic.subtopic.topic.subject.subject_name, 
                    "next_review": subtopic.next_review.isoformat(),
                })
            

            return JsonResponse({
                "should_review": True,
                "subtopics": subtopic_list
            })
        else:
            return JsonResponse({
                "should_review": False,
                "subtopics": []
            })


