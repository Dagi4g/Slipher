from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from Subjects import models, forms

class PlannedTopicsListView(ListView):
    model = models.Topics
    template_name = "Subjects/planned/planned_topic.html"
    context_object_name = "planned_topics"

    def get_queryset(self):
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
        topic = subject.topic.filter(subtopic__review=False)
        return topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject =  get_object_or_404(models.Subjects, id=self.kwargs.get('subject_id'))
        context['subject'] = subject
        context['planned_topic'] = subject.topic.filter(subtopic__review=False).distinct()
        return context
