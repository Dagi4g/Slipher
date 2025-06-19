

from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,get_list_or_404
from django.template import loader # for loding an html file and displaying it in the browserāo
from datetime import date
from django.http import JsonResponse
from django.utils import timezone
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt



from .models import Subjects,Topics,Subtopics,SubTopicMemory
from .forms import SubjectForm,TopicForm,SubtopicForm,SubtopicEntryForm

        ##---The Home Page---##

        ##---Subject related operation---##


        ##---topic related views.---##

        ##---Subtopic related views---##





from random import choice
from django.db.models import Prefetch
def show_planned_subject(request):
    subtopic = Subtopics.objects.filter(review=False)
    topic = Topics.objects.prefetch_related(Prefetch('subtopic',queryset=subtopic,to_attr='planned_subtopic'))
    subjects = Subjects.objects.prefetch_related(Prefetch('topic',queryset=topic,to_attr='planned_topic'))
    context = { 'subjects' : subjects,
                'topic' : topic,
                'subtopic' : subtopic,
               }
    template = loader.get_template('Subjects/planned/planned_subject.html')
    return HttpResponse(template.render(context,request))

def show_planned_topic(request,subject_id):
    subject = Subjects.objects.get(id=subject_id)

    topic = Topics.objects.filter(subject=subject,subtopic__review=False)

    template = loader.get_template('Subjects/planned/planned_topic.html')
    context = { 'subject': subject,
               'topic' : topic
               }
    return HttpResonse(template.render(context,request))

    



 
import json
@csrf_exempt
def remembered(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            subtopic_name = data.get("subtopic")
            if not subtopic_name:
                return HttpResponse("Missing subtopic", status=400)

            subtopic = Subtopics.objects.get(subtopic_name=subtopic_name)
            memory = SubTopicMemory.objects.get(subtopic=subtopic)

            memory.update_memory(remembered=True)
            memory.save()

            return HttpResponse(status=200)

        except (Subtopics.DoesNotExist, SubTopicMemory.DoesNotExist):
            return HttpResponse("Not found", status=404)
        except Exception as e:
            return HttpResponse(f"Server error: {e}", status=500)

    return HttpResponse("Invalid method", status=400)


@csrf_exempt
def forgot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            subtopic_name = data.get("subtopic")
            if not subtopic_name:
                return HttpResponse("Missing subtopic", status=400)

            subtopic = Subtopics.objects.get(subtopic_name=subtopic_name)
            memory = SubTopicMemory.objects.get(subtopic=subtopic)

            memory.update_memory(remembered=False)
            memory.save()

            return HttpResponse(status=200)

        except (Subtopics.DoesNotExist, SubTopicMemory.DoesNotExist):
            return HttpResponse("Not found", status=404)
        except Exception as e:
            return HttpResponse(f"Server error: {e}", status=500)

    return HttpResponse("Invalid method", status=400)
