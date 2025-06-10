from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from Subjects import models,forms


""" Handles subject-related view using djangos builtin class based view. (https://docs.djangoproject.com/en/5.2/topics/class-based-views/)
provides: 
    -Listing subjects (SubjectListView)
    -Creating subjects (SubjectCreateView),

AttributeError at /subject/1/topic/20/delete_topic/

'function' object has no attribute 'format'

Request Method: 	POST
Request URL: 	http://127.0.0.1:8000/subject/1/topic/20/delete_topic/
Django Version: 	4.2.21
Exception Type: 	AttributeError
Exception Value: 	

'function' object has no attribute 'format'

Exception Location: 	/home/et2050/.local/lib/python3.8/site-packages/django/views/generic/edit.py, line 238, in get_success_url
Raised during: 	Subjects.views0.topic.TopicDeleteView
Python Executable: 	/usr/bin/python3
Python Version: 	3.8.10
Python Path: 	

['/home/et2050/Slipher/App/Backend',
 '/usr/lib/python38.zip',
 '/usr/lib/python3.8',
 '/usr/lib/python3.8/lib-dynload',
 '/home/et2050/.local/lib/python3.8/site-packages',
 '/usr/local/lib/python3.8/dist-packages',
 '/usr/lib/python3/dist-packages']

Server time: 	Tue, 10 Jun 2025 08:32:23 +0000
Traceback Switch to copy-and-paste view

    /home/et2050/.local/lib/python3.8/site-packages/django/core/handlers/exception.py, line 55, in inner

                        response = get_response(request)

         …
    Local vars
    	
    	

    	

    	

    /home/et2050/.local/lib/python3.8/site-packages/django/core/handlers/base.py, line 197, in _get_response

                        response = wrapped_callback(request, *callback_args, **callback_kwargs)

         …
    Local vars
    	
    	

    	

    	

    	

    	

    	

    	

    	

    /home/et2050/.local/lib/python3.8/site-packages/django/views/generic/base.py, line 104, in view

                    return self.dispatch(request, *args, **kwargs)

         …
    Local vars
    	
    	

    	

    	

    	

    	

    	

    /home/et2050/.local/lib/python3.8/site-packages/django/views/generic/base.py, line 143, in dispatch

                return handler(request, *args, **kwargs)

         …
    Local vars
    	
    	

    	

    	

    	

    	

    /home/et2050/.local/lib/python3.8/site-packages/django/views/generic/edit.py, line 278, in post

                    return self.form_valid(form)

         …
    Local vars
    	
    	

    	

    	

    	

    	

    /home/et2050/.local/lib/python3.8/site-packages/django/views/generic/edit.py, line 283, in form_valid

                success_url = self.get_success_url()

         …
    Local vars
    	
    	

    	

    /home/et2050/.local/lib/python3.8/site-packages/django/views/generic/edit.py, line 238, in get_success_url

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


