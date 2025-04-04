from django import forms

from .models import Subjects

class SubjectForm(forms.ModelForm):
    """form.ModelForm is used to manage the database operations"""
    class Meta:
        model = Subjects
        fields= ['subject_name','rating']

