from rest_framework import serializers
from .models import Loss, Incident


class LossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loss
        fields = '__all__'


class IncidentSerializer(serializers.ModelSerializer):
    loss = LossSerializer()

    class Meta:
        model = Incident
        fields = '__all__'
