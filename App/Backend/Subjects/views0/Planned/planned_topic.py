from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from Subjects import models, forms

class PlannedTopicsListView(ListView):
    model = models.Topics
    template_name = "Subjects/planned/planned_topic.html"
    context_object_name = "planned_topics"

    def get_queryset(self):
        subject_id = self.kwargs.get('subject_id')
        subject = get_object_or_404(models.Subject, id=subject_id)
        return models.PlannedTopic.objects.filter(subject=subject).order_by('planned_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = get_object_or_404(models.Subject, id=self.kwargs.get('subject_id'))
        return context