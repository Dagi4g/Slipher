from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.template import loader # for loding an html file and displaying it in the browserāo


from .models import Subjects,Topics,Subtopics
from .forms import SubjectForm

def subject(requests):
    """Show the names of the subjects in the database."""
    subjects_list = Subjects.objects.all()
    template = loader.get_template("Subjects/subject.html")
    context = {
            "subjects_list" : subjects_list
            }
    return HttpResponse(template.render(context,requests))


def slipher(requests):
    return render(requests,"Subjects/slipher.html")

def topic(requests,subject_id):
    """show the topics of a particular subject."""
    subject = Subjects.objects.get(id=subject_id)#the name of the subject is needed inorder to show its topic.
    topic_list = subject.topics_set.all()
    template = loader.get_template("Subjects/topic.html")
    context = {
            "topic_list":topic_list,"subject":subject
            }
    return HttpResponse(template.render(context,requests))

def subtopics(requests,topic_id):
    """show all the availble subtopics in a perticular topic."""
    topic = Topics.objects.get(id=topic_id)
    subtopic_list = topic.subtopics_set.all()
    #get all the topics.
    template = loader.get_template("Subjects/subtopic.html")
    context = {
            "subtopic_list":subtopic_list,"topic":topic
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
            #the form is valid and saved so redirect the user to the home page.
            return redirect("Subjects:subject")
    template = loader.get_template("Subjects/new_subject.html")
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
    template = loader.get_template("Subjects/edit_subject.html")
    context =  {"form": form, "subject": subject}

    return HttpResponse(template.render(context,request))


def delete_subject(requests,subject_id):
    subject = get_object_or_404(Subjects,id=subject_id)
    if requests.method == "POST":
        subject.delete()
        return redirect("Subjects:subject")
    template = loader.get_template("Subjects/delete_subject.html")
    context = {"subject" : subject}
    return HttpResponse(template.render(context,requests))


