



from django.apps import AppConfig


class SubjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Subjects'
    
    def ready(self):
        import Subjects.signal
