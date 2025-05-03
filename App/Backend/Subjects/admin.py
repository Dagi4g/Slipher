from django.contrib import admin

from .models import Subjects,Topics,Subtopics,SubtopicEntry

admin.site.register(Subjects)
admin.site.register(Topics)
admin.site.register(Subtopics)
admin.site.register(SubtopicEntry)
