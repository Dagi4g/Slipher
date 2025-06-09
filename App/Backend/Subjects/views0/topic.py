from django.views.generic import ListView,CreateView,DeleteView
from django.shortcuts import get_object_or_404
from Subjects import models,forms

class TopicListView(ListView):
    model = models.Topics
    template_name = "Subjects/topic/topic.html"
    context_object_name = "topic_list"

    def get_queryset(self):
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
        topic_list = subject.topic.all()
        return topic_list

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["subject"] = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
        print(context)
        return context

