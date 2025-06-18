from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404,HttpResponse
from django.urls import reverse_lazy
from django.db.utils import IntegrityError

from Subjects import models,forms

class SubtopicListView(ListView):
    model = models.Subtopics
    template_name = "Subjects/subtopic/subtopic.html"
    context_name = "subtopic_list"
    
    def get_queryset(self):
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
        topic = subject.topic.get(id=self.kwargs["topic_id"])
        subtopic = topic.subtopic.all()
        return subtopic

    def get_context_data(self,**kwargs):
        subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
        topic = subject.topic.get(id=self.kwargs["topic_id"])
        subtopic_list = topic.subtopic.all()
        context = super().get_context_data(**kwargs)
        context["subject"] = subject
        context["topic"] = topic
        context["subtopic_list"] = subtopic_list
        return context

class SubtopicCreateView(CreateView):
     model = models.Subtopics
     template_name = 'Subjects/subtopic/new_subtopic.html'
     form_class = forms.SubtopicForm

     def get_success_url(self):
         return reverse_lazy("Subject:subtopic",kwargs={"subject_id":self.kwargs["subject_id"],"topic_id":self.kwargs["topic_id"]})

     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
         topic = subject.topic.get(id=self.kwargs["topic_id"])
         context["subject"], context["topic"] = subject, topic
         return context

     def form_valid(self,form):
         subject = get_object_or_404(models.Subjects,id=self.kwargs["subject_id"])
         topic = subject.topic.get(id=self.kwargs["topic_id"])
         form.instance.topic = topic
         try:
             return super().form_valid(form)
         except IntegrityError:
             return HttpResponse(f"{form.cleaned_data['subtopic_name']} already exists")

      
        

