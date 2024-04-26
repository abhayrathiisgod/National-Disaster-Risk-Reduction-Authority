from rest_framework import serializers
from .models import Officer, Designation


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class OfficerSerializer(serializers.ModelSerializer):
    # Use many=True for ForeignKey relationships
    designationss = DesignationSerializer(many=True)

    class Meta:
        model = Officer
        fields = ['id', 'name', 'name_ne', 'additional_info',
                  'additional_info_ne', 'image', 'order', 'designationss']
