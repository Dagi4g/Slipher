from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.db.utils import IntegrityError

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
        entries = subtopic.subtopicentry.filter(subtopic=subtopic)
        context['entries'] = entries
        context['subject'] = subject
        context['topic'] = topic
        context['subtopic'] = subtopic
        return context

class SubtopicEntryCreateView(CreateView):
    model = models.SubtopicEntry
    form_class = forms.SubtopicEntryForm
    template_name = 'Subjects/subtopic/entry/new_entry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])    
        topic  = get_object_or_404(models.Topics,id=self.kwargs["topic_id"])
        subtopic = get_object_or_404(models.Subtopics,id=self.kwargs["subtopic_id"])
        context['subject'] = subject
        context['topic'] = topic
        context['subtopic'] = subtopic
        return context
    
    def get_success_url(self):
        return reverse_lazy("Subjects:subtopic_entry", kwargs={
            "subject_id": self.kwargs["subject_id"],
            "topic_id": self.kwargs["topic_id"],
            "subtopic_id": self.kwargs["subtopic_id"]
        })
    
    def form_valid(self, form):
        subject = get_object_or_404(models.Subjects, id=self.kwargs["subject_id"])
        topic = get_object_or_404(models.Topics, id=self.kwargs["topic_id"])
        subtopic = get_object_or_404(models.Subtopics, id=self.kwargs["subtopic_id"])
        form.instance.subtopic = subtopic
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse(f"{form.cleaned_data['entry_name']} already exists in this subtopic")
        
class SubtopicEntryUpdateView(UpdateView):
    model = models.SubtopicEntry
    form_class = forms.SubtopicEntryForm
    template_name = 'Subjects/subtopic/entry/edit_entry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])    
        topic  = get_object_or_404(models.Topics,id=self.kwargs["topic_id"])
        subtopic = get_object_or_404(models.Subtopics,id=self.kwargs["subtopic_id"])
        entry = get_object_or_404(models.SubtopicEntry, id=self.kwargs['entry_id'])
        context['subject'] = subject
        context['topic'] = topic
        context['subtopic'] = subtopic
        context['entry'] = entry
        return context
    
    def get_success_url(self):
        return reverse_lazy("Subjects:subtopic_entry", kwargs={
            "subject_id": self.kwargs["subject_id"],
            "topic_id": self.kwargs["topic_id"],
            "subtopic_id": self.kwargs["subtopic_id"]
        })  
    def get_object(self):
        return get_object_or_404(models.SubtopicEntry, id=self.kwargs['entry_id'])
    
class SubtopicEntryDeleteView(DeleteView):
    model = models.SubtopicEntry
    template_name = 'Subjects/subtopic/entry/delete_entry.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])    
        topic  = get_object_or_404(models.Topics,id=self.kwargs["topic_id"])
        subtopic = get_object_or_404(models.Subtopics,id=self.kwargs["subtopic_id"])
        entry = get_object_or_404(models.SubtopicEntry, id=self.kwargs['entry_id'])
        context['subject'] = subject
        context['topic'] = topic
        context['subtopic'] = subtopic
        context['entry'] = entry
        return context
    
    def get_success_url(self):
        return reverse_lazy("Subjects:subtopic_entry", kwargs={
            "subject_id": self.kwargs["subject_id"],
            "topic_id": self.kwargs["topic_id"],
            "subtopic_id": self.kwargs["subtopic_id"]
        })
    def get_object(self):
        return get_object_or_404(models.SubtopicEntry, id=self.kwargs['entry_id'])