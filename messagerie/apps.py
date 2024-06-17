from django.apps import AppConfig


class MessagerieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'messagerie'
    
    def ready(self):
        import messagerie.signals
