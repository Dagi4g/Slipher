from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from Subjects import models,forms


""" Handles subject-related view using djangos builtin class based view. (https://docs.djangoproject.com/en/5.2/topics/class-based-views/)
provides: 
    -Listing subjects (SubjectListView)
    -Creating subjects (SubjectCreateView),
    -Editing subjects (SubjectEditView),
    -Deleting subjects (SubjectDelteView)

see django documentation for more in class-based-view:
https://docs.djangoproject.com/en/5.2/topics/class-based-views/
"""
class SubjectListView(ListView):
    model = models.Subjects
    template_name = "Subjects/subjects/subject.html"
    context_object_name = "subjects_list"

class SubjectCreateView(CreateView):
    model = models.Subjects
    template_name = "Subjects/subjects/new_subject.html"
    form_class = forms.SubjectForm
    success_url = reverse_lazy("Subjects:subject")


class SubjectUpdateView(UpdateView):
    model = models.Subjects
    template_name = "Subjects/subjects/edit_subject.html"
    form_class = forms.SubjectForm
    success_url = reverse_lazy("Subjects:subject")

class SubjectDeleteView(DeleteView):
    model = models.Subjects
    template_name = "Subjects/subjects/delete_subject.html"
    success_url = reverse_lazy("Subjects:subject")

    def get_object(self):
        """get the Subject to delete from the url"""
        return get_object_or_404(models.Subjects,pk=self.kwargs["subject_id"])


