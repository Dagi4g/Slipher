from django.urls import path,include

from . import views

urlpatterns = [
        #home page for slipher.
        path("",views.slipher,name="slipher"),
        #show the list of subjects.
        path("subject",views.subject,name="subject"),
        #show the list of topics.
        path("subject/<int:subject_id>/",views.topic,name="topic"),
        #show the list of subtopics.
        path("topic/<int:topic_id>/",views.subtopics,name="subtopic"),

        ]
