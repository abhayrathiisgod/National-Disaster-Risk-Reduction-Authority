from django.apps import AppConfig


class PressnotenewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pressnotenews"

    def ready(self):
        import pressnotenews.signals
