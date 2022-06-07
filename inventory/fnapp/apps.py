from django.apps import AppConfig


class FnappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fnapp'

    def ready(self):
        import fnapp.signals
