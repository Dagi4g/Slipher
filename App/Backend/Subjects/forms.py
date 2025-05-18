from django import forms

from .models import Subjects,Topics,Subtopics,SubtopicEntry

class SubjectForm(forms.ModelForm):
    """form.ModelForm is used to manage the database operations"""
    class Meta:
        model = Subjects
        fields= ['subject_name','rating']
       

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topics
        fields = ['topic_name','rating']

class SubtopicForm(forms.ModelForm):
    class Meta:
        model = Subtopics
        fields = [ 'subtopic_name', 'last_seen','rating','review']

class SubtopicEntryForm(forms.ModelForm):
    class Meta:
        model = SubtopicEntry
        fields = [ 'text' ]
