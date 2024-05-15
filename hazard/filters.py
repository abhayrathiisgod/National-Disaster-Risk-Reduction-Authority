import django_filters
from .models import Hazards


class HazardFilter(django_filters.FilterSet):
    class Meta:
        model = Hazards
        fields = {
            'type': ['exact'],
        }
