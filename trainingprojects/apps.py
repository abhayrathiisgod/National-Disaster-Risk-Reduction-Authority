from django.apps import AppConfig


class TrainingprojectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "trainingprojects"

    def ready(self):
        import trainingprojects.signals
