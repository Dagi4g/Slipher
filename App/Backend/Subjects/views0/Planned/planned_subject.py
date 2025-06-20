from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from Subjects import models
class PlannedSubjectsListView(ListView):
    model = models.Subjects
    template_name = 'Subjects/planned/planned_subject.html'
    context_object_name = 'planned_subjects'

    def get_queryset(self):
        subtopic = models.Subtopics.objects.filter(review=False)
        topic = models.Topics.objects.prefetch_related(Prefetch('subtopic', queryset=subtopic, to_attr='planned_subtopic'))
        subject = models.Subjects.objects.prefetch_related(Prefetch('topic', queryset=topic, to_attr='planned_topic'))
        return subject.order_by('subject_name')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['planned_subjects'] = self.get_queryset()
        print(context['planned_subjects'])
        return context