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


class RememberedView(View):
    def post(self, request):
        data = json.loads(request.body)
        subtopic_name = data.get("subtopic")
        if not subtopic_name:
            return JsonResponse({"error": "Subtopic name is required"}, status=400)

        try:
            subtopic = models.Subtopics.objects.get(subtopic_name=subtopic_name)
            memory, created = models.SubTopicMemory.objects.get_or_create(subtopic=subtopic)

            if created:
                memory.update_memory(remembered=True) # Set next review to 1 day later
                memory.save()
                return JsonResponse({"message": "Subtopic marked as remembered"})
            else:
                return JsonResponse({"message": "Subtopic already marked as remembered"})

        except models.Subtopics.DoesNotExist:
            return JsonResponse({"error": "Subtopic not found"}, status=404)
        
class ForgotView(View):
    def post(self, request):
        data = json.loads(request.body)
        subtopic_name = data.get("subtopic")
        if not subtopic_name:
            return JsonResponse({"error": "Subtopic name is required"}, status=400)

        try:
            subtopic = models.Subtopics.objects.get(subtopic_name=subtopic_name)
            memory, created = models.SubTopicMemory.objects.get_or_create(subtopic=subtopic)

            if created:
                memory.update_memory(remembered=False) # the user  doesnt remember the subtopic, so we set next review to 0 days later
                memory.save()
                return JsonResponse({"message": "Subtopic marked as forgotten"})
            else:
                return JsonResponse({"message": "Subtopic already marked as forgotten"})

        except models.Subtopics.DoesNotExist:
            return JsonResponse({"error": "Subtopic not found"}, status=404)