from django.apps import AppConfig
from bulletin.models import Bulletin


class YourAppConfig(AppConfig):
    name = 'bulletin'

    def ready(self):
        import bulletin.signals
