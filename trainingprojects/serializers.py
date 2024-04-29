from rest_framework import serializers
from .models import Address, Donater, Project
from federal.serializers import DistrictSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DonaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donater
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    # donor = DonaterSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Project
        fields = ['id', 'address', 'created_at', 'updated_at', 'deleted_at', 'title', 'title_ne',
                  'budget', 'budget_ne', 'start_date', 'end_date', 'created_by', 'updated_by', 'district']


class ProjectDetailSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    donor = DonaterSerializer()
    district = DistrictSerializer()

    class Meta:
        model = Project
        fields = ['id', 'address', 'donor', 'created_at', 'updated_at', 'deleted_at', 'title', 'title_ne',
                  'budget', 'budget_ne', 'start_date', 'end_date', 'created_by', 'updated_by', 'district']
