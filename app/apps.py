from django.apps import AppConfig as BaseAppConfig
from django.db.models.signals import post_save


class AppConfig(BaseAppConfig):
    name = "app"

    def ready(self):
        from .signals import generate_check
        post_save.connect(generate_check, sender=self.get_model('Check'))
