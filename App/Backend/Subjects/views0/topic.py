from django.views.generic import ListView,CreateView,DeleteView
from django.shortcuts import get_object_or_404,HttpResponse
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

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
        return context

class TopicCreateView(CreateView):
    model = models.Topics
    template_name = "Subjects/topic/new_topic.html"
    form_class = forms.TopicForm

    def get_success_url(self):
        return reverse_lazy("Subjects:topic",kwargs={'subject_id':self.kwargs['subject_id']})
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["subject"] = get_object_or_404(models.Subjects,pk=self.kwargs['subject_id'])
        return context

    def form_valid(self,form):
        subject = get_object_or_404(models.Subjects,id=self.kwargs['subject_id'])
        form.instance.subject = subject
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse(f"{form.cleaned_data['topic_name']} already exists")
