from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, HttpResponse
from django.urls import reverse_lazy
from django.db.utils import IntegrityError  

from Subjects import models, forms

class PlannedSubtopicListView(ListView):
    model = models.Subtopics
    template_name = "Subjects/planned/planned_subtopic.html"
    context_name = "planned_subtopics"

    def get_queryset(self):
        subject = get_object_or_404(models.Subjects, id=self.kwargs["subject_id"])
        topic = subject.topic.get(id=self.kwargs["topic_id"])
        subtopic = topic.subtopic.filter(review=False)
        return subtopic
    
    def get_context_data(self, **kwargs):  
        subject = get_object_or_404(models.Subjects, id=self.kwargs["subject_id"])
        topic = subject.topic.get(id=self.kwargs["topic_id"])
        subtopic_list = topic.subtopic.filter(review=False)
        context = super().get_context_data(**kwargs)
        context["subject"] = subject
        context["topic"] = topic
        context["planned_subtopics"] = subtopic_list
        return context