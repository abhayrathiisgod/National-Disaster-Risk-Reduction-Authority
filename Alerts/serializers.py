from rest_framework import serializers
from .models import AlertList


class AlertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertList
        fields = ['id', 'title', 'wards', 'point', 'createdOn', 'titleNe', 'source', 'description', 'verified', 'public', 'startedOn', 'expireOn',
                  'polygon', 'referenceType', 'referenceData', 'referenceId', 'region', 'regionId', 'createdBy', 'updatedBy', 'hazard', 'event']
