import django_filters
from .models import EmergencyVehicle


class EmergencyVehicleFilter(django_filters.FilterSet):
    vehicle_type = django_filters.ChoiceFilter(choices=EmergencyVehicle.type)

    class Meta:
        model = EmergencyVehicle
        fields = ['vehicle_type']
