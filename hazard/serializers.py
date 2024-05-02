from rest_framework import serializers
from .models import Hazards


class HazardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hazards
        fields = ['id', 'title', 'title_ne', 'description',
                  'order', 'color', 'icon', 'type']
