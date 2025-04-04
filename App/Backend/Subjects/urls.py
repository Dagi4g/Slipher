from django.urls import path,include

from . import views

app_name = "Subjects"

urlpatterns = [
        #home page for slipher.
        path("",views.slipher,name="slipher"),
        #show the list of subjects.
        #"""subject_related"""
        path("subject",views.subject,name="subject"),
        #add new subject
        path("subject/new_subject",views.new_subject,name="new_subject"),
        #edit existing subject
        path("subject/<int:subject_id>/edit_subject",views.edit_subject,name="edit_subject"),
        #delte an existing subject.
        path("subject/<int:subject_id>/delete_subject",views.delete_subject,name="delete_subject"),

        #"""topic related"""
        #show the list of topics.
        path("subject/<int:subject_id>/",views.topic,name="topic"),
        #"""subtopic_related"""
        #show the list of subtopics.
        path("topic/<int:topic_id>/",views.subtopics,name="subtopic"),

        ]
