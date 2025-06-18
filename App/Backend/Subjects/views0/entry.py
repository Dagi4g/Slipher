from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from Subjects import models , forms
from django.http import HttpResponse
class SubtopicEntryListView(ListView):
    model = models.SubtopicEntry
    template_name = 'Subjects/subtopic/entry/show_entry.html'
    context_object_name = 'entries'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs['subject_id']
        topic_id = self.kwargs['topic_id']
        subtopic_id = self.kwargs['subtopic_id']
        context['subject'] = Subjects.objects.get(id=subject_id)
        context['topic'] = Topics.objects.get(id=topic_id)
        context['subtopic'] = Subtopics.objects.get(id=subtopic_id)
        return context