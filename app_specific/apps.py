from django.apps import AppConfig


class AppSpecificConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_specific'
