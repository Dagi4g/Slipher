from django.db.models import Q, Exists, OuterRef
from django.views.generic import ListView
from Subjects import models

class PlannedSubjectsListView(ListView):
    model = models.Subjects
    template_name = 'Subjects/planned/planned_subject.html'
    context_object_name = 'planned_subject'

    def get_queryset(self):
        # Subjects with at least one subtopic where review=False
        planned_subtopic_qs = models.Subtopics.objects.filter(
            topic__subject=OuterRef('pk'),
            review=False
        )     
        # Subjects with no topics or no subtopics
        no_topic_or_subtopic_q = (
            Q(topic__isnull=True) |
            Q(topic__subtopic__isnull=True)
        )
        queryset = models.Subjects.objects.annotate(
            has_planned_subtopic=Exists(planned_subtopic_qs)
        ).filter(
            Q(has_planned_subtopic=True) | no_topic_or_subtopic_q
        ).distinct().order_by('subject_name')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_queryset()[1].has_planned_subtopic)
        context['planned_subjects'] = self.get_queryset()
        return context