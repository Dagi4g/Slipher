

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
def subject(requests):
    """Show the names of the subjects in the database."""
    subjects_list = Subjects.objects.all()
    template = loader.get_template("Subjects/subjects/subject.html")
    context = {
            "subjects_list" : subjects_list
            }
    return HttpResponse(template.render(context,requests))

def new_subject(requests):
    """add new subject to the database"""
    if requests.method != "POST":
        #the user didn't add any data,so create a blank form.
        form = SubjectForm()
    else:
        form = SubjectForm(requests.POST)
        if form.is_valid():
            form.save()
            #the form is valid and saved so redirect the user to the list of subjects.
            return redirect("Subjects:subject")
    template = loader.get_template("Subjects/subjects/new_subject.html")
    context = {"form" : form}
    return HttpResponse(template.render(context,requests))# just show the form.


def edit_subject(request, subject_id): 
    subject = get_object_or_404(Subjects, id=subject_id)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.instance.subject_name = subject.subject_name  # Ensure subject name remains the same
            form.save()
            return redirect("Subjects:subject")
    else:
        form = SubjectForm(instance=subject)
    template = loader.get_template("Subjects/subjects/edit_subject.html")
    context =  {"form": form, "subject": subject}

    return HttpResponse(template.render(context,request))


def delete_subject(requests,subject_id):
    subject = get_object_or_404(Subjects,id=subject_id)
    if requests.method == "POST":
        subject.delete()
        return redirect("Subjects:subject")
    template = loader.get_template("Subjects/subjects/delete_subject.html")
    context = {"subject" : subject}
    return HttpResponse(template.render(context,requests))


        ##---topic related views.---##
def topic(requests,subject_id):
    """show the topics of a particular subject."""
    subject = Subjects.objects.get(id=subject_id)#the name of the subject is needed inorder to show its topic.
    topic_list = subject.topic.all()
    template = loader.get_template("Subjects/topic/topic.html")
    context = {
            "topic_list":topic_list,"subject":subject
            }
    return HttpResponse(template.render(context,requests))

# Add Topic
def new_topic(request,subject_id):
    subject = get_object_or_404(Subjects,id=subject_id)
    if request.method == 'POST':
        form = TopicForm(request.POST,initial={'subject':subject})
        if form.is_valid():
            try:
                topic = form.save(commit=False)
                topic.subject = subject
                topic.save()
            except IntegrityError :
                return HttpResponse(f"{topic.topic_name} already exists")
            return redirect('Subjects:topic',subject_id=subject_id)
    else:
        form = TopicForm()
    template = loader.get_template("Subjects/topic/new_topic.html")
    context = {"form":form,'subject':subject}
    return HttpResponse(template.render(context,request))
# Edit Subtopic
def edit_subtopic(request, subtopic_id, topic_id, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)

    if request.method == 'POST':
        form = SubtopicForm(request.POST, instance=subtopic)
        if form.is_valid():
            form.instance.topic = topic  # ensure topic is set
            form.save()
            return redirect('Subjects:subtopic', subject_id=subject_id, topic_id=topic_id)
    else:
        form = SubtopicForm(instance=subtopic)

    template = loader.get_template('Subjects/subtopic/edit_subtopic.html')
    context = {'form': form, 'subtopic': subtopic, 'topic': topic, 'subject': subject}
    return HttpResponse(template.render(context, request))

# Edit Topic
def edit_topic(request, topic_id,subject_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.instance.topic_name = topic.topic_name
            form.save()
            return redirect('Subjects:topic',subject_id=subject_id)
    else:
        form = TopicForm(instance=topic)

    template = loader.get_template('Subjects/topic/edit_topic.html')
    context = {'form':form,'topic':topic,'subject':subject}
    return HttpResponse(template.render(context,request))

# Delete Topic
def delete_topic(request, subject_id,topic_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)

    if request.method == "POST":
        topic.delete()
        return redirect("Subjects:topic",subject_id=subject_id)
    template = loader.get_template("Subjects/topic/delete_topic.html")
    context = {"subject" : subject,'topic':topic}
    return HttpResponse(template.render(context,request))


        ##---Subtopic related views---##

def subtopics(requests,subject_id,topic_id):
    """show all the availble subtopics in a perticular topic."""
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic_list = topic.subtopic.all()
    #get all the topics.
    template = loader.get_template("Subjects/subtopic/subtopic.html")
    context = {
            "subtopic_list":subtopic_list,"topic":topic,"subject":subject
            }
    return HttpResponse(template.render(context,requests))

# Add Subtopic
def new_subtopic(request,subject_id,topic_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    last_seen = date.today().isoformat()
    initial_data = { 'last_seen':last_seen}
    if request.method == 'POST':
        form = SubtopicForm(request.POST,initial=initial_data)
        if form.is_valid():
            subtopic = form.save(commit=False)
            subtopic.topic = topic
            subtopic.save()
            return redirect("Subjects:subtopic",subject_id=subject_id,topic_id=topic_id )
    else:
        form = SubtopicForm(initial=initial_data)
    template = loader.get_template('Subjects/subtopic/new_subtopic.html')
    context = {'form':form,'subject':subject,'topic':topic,}
    return HttpResponse(template.render(context,request))
def edit_subtopic(request, subtopic_id, topic_id, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)

    if request.method == 'POST':
        form = SubtopicForm(request.POST, instance=subtopic)
        if form.is_valid():
            form.instance.topic = topic  # ensure topic is set
            form.save()
            return redirect('Subjects:subtopic', subject_id=subject_id, topic_id=topic_id)
    else:
        form = SubtopicForm(instance=subtopic)

    template = loader.get_template('Subjects/subtopic/edit_subtopic.html')
    context = {'form': form, 'subtopic': subtopic, 'topic': topic, 'subject': subject}
    return HttpResponse(template.render(context, request))

# Delete Subtopic
def delete_subtopic(request, subject_id,topic_id,subtopic_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)

    if request.method == "POST":
        subtopic.delete()
        return redirect("Subjects:subtopic",subject_id=subject_id,topic_id=topic_id)
    template = loader.get_template("Subjects/subtopic/delete_subtopic.html")
    context = {"subject" : subject,'topic':topic,"subtopic":subtopic}
    return HttpResponse(template.render(context,request))

#subtopic entry.
def entry(requests,subject_id,topic_id,subtopic_id):
    #for displaying additional information about the subtoic the user entered.
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)
    entries = subtopic.subtopicentry.all()
    #get all the entries.
    template = loader.get_template("Subjects/subtopic/entry/show_entry.html")
    context = {
            "subtopic":subtopic,"topic":topic,"subject":subject,"entries":entries,
            }
    return HttpResponse(template.render(context,requests))




# adding entry.

def new_entry(request,subject_id,topic_id,subtopic_id):
    """Add creating new text data about a particular subtopic"""
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)
    if request.method == 'POST':
        form = SubtopicEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.subtopic = subtopic
            entry.save()
            return redirect("Subjects:subtopic_entry",subject_id=subject_id,topic_id=topic_id ,subtopic_id=subtopic_id)
    else:
        form = SubtopicEntryForm()
    template = loader.get_template('Subjects/subtopic/entry/new_entry.html')
    context = {'form':form,'subject':subject,'topic':topic,"subtopic":subtopic}
    return HttpResponse(template.render(context,request))

# editing entry.
def edit_entry(request, subtopic_id, topic_id, subject_id,entry_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)
    entry = subtopic.subtopicentry.get(id=entry_id)
    print(entry.id)

    if request.method == 'POST':
        form = SubtopicEntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.instance.subtopic = subtopic  # ensure topic is set
            form.save()
            return redirect('Subjects:subtopic_entry', subject_id=subject_id, topic_id=topic_id, subtopic_id=subtopic_id,)
    else:
        form = SubtopicEntryForm(instance=entry)

    template = loader.get_template('Subjects/subtopic/entry/edit_entry.html')
    context = {'form': form, 'entry':entry,'subtopic': subtopic, 'topic': topic, 'subject': subject}
    return HttpResponse(template.render(context, request))



# Delete entry
def delete_entry(request, subject_id,topic_id,subtopic_id,entry_id):
    subject = Subjects.objects.get(id=subject_id)
    topic = subject.topic.get(id=topic_id)
    subtopic = topic.subtopic.get(id=subtopic_id)
    entry = subtopic.subtopicentry.get(id=entry_id)

    if request.method == "POST":
        entry.delete()
        return redirect("Subjects:subtopic_entry",subject_id=subject_id,topic_id=topic_id, subtopic_id=subtopic.id)
    template = loader.get_template("Subjects/subtopic/entry/delete_entry.html")
    context = { "entry":entry,"subject" : subject,'topic':topic,"subtopic":subtopic}
    return HttpResponse(template.render(context,request))




from random import choice

def should_review(request):
    now = date.today()

    # Filter subtopics where review date/time is <= now (due for review)
    due_subtopics = SubTopicMemory.objects.filter(next_review__lte=now)

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
            memory = SubTopicMemory.objects.get(id=subtopic.id)

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
            memory = SubTopicMemory.objects.get(id=subtopic.id)

            memory.update_memory(remembered=False)
            memory.save()

            return HttpResponse(status=200)

        except (Subtopics.DoesNotExist, SubTopicMemory.DoesNotExist):
            return HttpResponse("Not found", status=404)
        except Exception as e:
            return HttpResponse(f"Server error: {e}", status=500)

    return HttpResponse("Invalid method", status=400)
