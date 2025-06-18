from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy

from Subjects import models , forms

class SubtopicEntryListView(ListView):
    model = models.SubtopicEntry
    template_name = 'Subjects/subtopic/entry/show_entry.html'
    context_object_name = 'entries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])    
        topic  = get_object_or_404(models.Topics,id=self.kwargs["topic_id"])
        subtopic = get_object_or_404(models.Subtopics,id=self.kwargs["subtopic_id"])
        entries = subtopic.subtopicentry.all()
        context['subject'] = subject
        context['topic'] = topic
        context['subtopic'] = subtopic
        context["entries"] = entries
        return context
