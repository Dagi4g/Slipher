



from django.urls import path,include

from . import views
from . import views0

app_name = "Subjects"

urlpatterns = [
        #home page for slipher.
        path("",views0.slipher,name="slipher"),
        #show the list of subjects.
        ##---subject_related---##
        path("slipher/subject",views0.SubjectListView.as_view(),name="subject"),
        #add new subject
        path("subject/new_subject",views0.SubjectCreateView.as_view(),name="new_subject"),
        #edit existing subject
        path("subject/<int:subject_id>/edit_subject",views0.SubjectUpdateView.as_view(),name="edit_subject"),
        #delte an existing subject.
        path("subject/<int:subject_id>/delete_subject",views0.SubjectDeleteView.as_view(),name="delete_subject"),


        ##---topic related---##
        #show the list of topics.
        path("subject/<int:subject_id>/topic",views0.TopicListView.as_view(),name="topic"),
        path("subject/<int:subject_id>/topic/new_topic",views0.TopicCreateView.as_view(),name="new_topic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/edit_topic/",views0.TopicUpdateView.as_view(),name="edit_topic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/delete_topic/",views0.TopicDeleteView.as_view(),name="delete_topic"),


        ##---subtopic_related---##
        #show the list of subtopics.
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic",views0.SubtopicListView.as_view(),name="subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/new_subtopic",views0.SubtopicCreateView.as_view(),name="new_subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/edit_subtopic",views0.SubtopicUpdateView.as_view(),name="edit_subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/delete_subtopic",views0.SubtopicDeleteView.as_view(),name="delete_subtopic"),

        ##---entry---##
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/subtopic_entry",views.entry,name="subtopic_entry"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/new_entry",views.new_entry,name="new_entry"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/subtopic_entry/<int:entry_id>/edit_entry",views.edit_entry,name="edit_entry"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/subtopic_entry/<int:entry_id>/delete_entry",views.delete_entry,name="delete_entry"),


        ##---show review---##
        path("should_review/",views.should_review,name="should_review"),

        path("remembered/",views.remembered,name="rememebered"),
        path("forgot/",views.forgot,name="forgot"),

        ##---plan---##
        path("planned_subject",views.show_planned_subject,name='planned_subject'),
        path("planned_subject/<int:subject_id>/planned_topic",views.show_planned_subject,name='planned_subject'),

        ]

