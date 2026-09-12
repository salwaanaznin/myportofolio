from django.apps import AppConfig
import sys

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Mencegah komando berjalan saat jalankan makemigrations/migrate
        if 'runserver' in sys.argv or 'gunicorn' in sys.argv[0]:
            from django.core.management import call_command
            try:
                call_command('loaddata', 'initial_experiences.json')
            except Exception:
                pass