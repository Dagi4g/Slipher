from django.urls import path,include

from . import views

app_name = "Subjects"

urlpatterns = [
        #home page for slipher.
        path("",views.slipher,name="slipher"),
        #show the list of subjects.
        ##---subject_related---##
        path("slipher/subject",views.subject,name="subject"),
        #add new subject
        path("subject/new_subject",views.new_subject,name="new_subject"),
        #edit existing subject
        path("subject/<int:subject_id>/edit_subject",views.edit_subject,name="edit_subject"),
        #delte an existing subject.
        path("subject/<int:subject_id>/delete_subject",views.delete_subject,name="delete_subject"),


        ##---topic related---##
        #show the list of topics.
        path("subject/<int:subject_id>/topic",views.topic,name="topic"),
        path("subject/<int:subject_id>/topic/new_topic",views.new_topic,name="new_topic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/edit_topic/",views.edit_topic,name="edit_topic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/delete_topic/",views.delete_topic,name="delete_topic"),


        ##---subtopic_related---##
        #show the list of subtopics.
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic",views.subtopics,name="subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/new_subtopic",views.new_subtopic,name="new_subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/edit_subtopic",views.edit_subtopic,name="edit_subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/delete_subtopic",views.delete_subtopic,name="delete_subtopic"),


        ##---show review---##
        path("should_review/",views.should_review,name="should_review")

        ]
