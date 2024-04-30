from rest_framework import serializers
from .models import Hazards


class HazardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hazards
        fields = '__all__'
