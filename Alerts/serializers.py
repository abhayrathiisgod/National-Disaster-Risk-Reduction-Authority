from rest_framework import serializers
from .models import AlertList


class AlertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertList
        fields = '__all__'
