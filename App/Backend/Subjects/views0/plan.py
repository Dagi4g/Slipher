from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import HttpResponse,get_object_or_404
from django.urls import reverse_lazy

from Subjects import models,forms

class PlanedSubjectView(ListView):
    models = models.Subjects
    template_name = "Subjects/planned/"
