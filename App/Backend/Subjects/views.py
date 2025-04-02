from django.shortcuts import render,HttpResponse
from django.template import loader # for loding an html file and displaying it in the browserāo


from .models import Subjects,Topics,Subtopics


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


