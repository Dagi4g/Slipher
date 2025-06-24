



from django.urls import path,include

from . import views

app_name = "Subjects"

urlpatterns = [
        #home page for slipher.
        path("",views.slipher,name="slipher"),
        #show the list of subjects.
        ##---subject_related---##
        path("slipher/subject",views.SubjectListView.as_view(),name="subject"),
        #add new subject
        path("subject/new_subject",views.SubjectCreateView.as_view(),name="new_subject"),
        #edit existing subject
        path("subject/<int:subject_id>/edit_subject",views.SubjectUpdateView.as_view(),name="edit_subject"),
        #delte an existing subject.
        path("subject/<int:subject_id>/delete_subject",views.SubjectDeleteView.as_view(),name="delete_subject"),


        ##---topic related---##
        #show the list of topics.
        path("subject/<int:subject_id>/topic",views.TopicListView.as_view(),name="topic"),
        path("subject/<int:subject_id>/topic/new_topic",views.TopicCreateView.as_view(),name="new_topic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/edit_topic/",views.TopicUpdateView.as_view(),name="edit_topic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/delete_topic/",views.TopicDeleteView.as_view(),name="delete_topic"),


        ##---subtopic_related---##
        #show the list of subtopics.
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic",views.SubtopicListView.as_view(),name="subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/new_subtopic",views.SubtopicCreateView.as_view(),name="new_subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/edit_subtopic",views.SubTopicUpdateView.as_view(),name="edit_subtopic"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/delete_subtopic",views.SubTopicDeleteView.as_view(),name="delete_subtopic"),

        ##---entry---##
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/subtopic_entry",views.SubtopicEntryListView.as_view(),name="subtopic_entry"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/new_entry",views.SubtopicEntryCreateView.as_view(),name="new_entry"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/subtopic_entry/<int:entry_id>/edit_entry",views.SubtopicEntryUpdateView.as_view(),name="edit_entry"),
        path("subject/<int:subject_id>/topic/<int:topic_id>/subtopic/<int:subtopic_id>/subtopic_entry/<int:entry_id>/delete_entry",views.SubtopicEntryDeleteView.as_view(),name="delete_entry"),



        ##---show review---##
        path("should_review/",views.ShouldReviewView.as_view(),name="should_review"),

        path("remembered/",views.RememberedView.as_view(),name="rememebered"),
        path("forgot/",views.ForgotView.as_view(),name="forgot"),

        ##---plan---##
        path("planned_subject",views.PlannedSubjectsListView.as_view(),name='planned_subject'),
        path("planned_subject/new_planned_subject",views.PlannedSubjectCreateView.as_view(),name='new_planned_subject'),
        path("planned_subject/<int:subject_id>/planned_topic",views.PlannedTopicsListView.as_view(),name='planned_topic'),
        path("planned_subject/<int:subject_id>/planned_topic/<int:topic_id>/planned_subtopic", views.PlannedSubtopicListView.as_view(), name='planned_subtopic'),


        ]

