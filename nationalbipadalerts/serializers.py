from rest_framework import serializers
from profiles.serializers import OfficerProfileSerializer, OfficerProfileforalertSerializer

from . import models


class ImportantLInksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImportantLinks
        fields = '__all__'


class BipadAlertsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BipadAlerts
        fields = '__all__'


class BipadAlertsSerializer(serializers.ModelSerializer):
    important_links = ImportantLInksSerializer(many=True)
    important_numbers = OfficerProfileforalertSerializer(many=True)

    class Meta:
        model = models.BipadAlerts
        fields = '__all__'
