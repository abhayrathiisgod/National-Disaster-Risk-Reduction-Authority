from rest_framework import serializers
from .models import Address, Donater, Project, Training, GeoHazardAssessment, fiscal
from federal.serializers import DistrictSerializer, MunicipalityySerializer, ProvinceSerializer
from datetime import date


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
    district = DistrictSerializer()

    class Meta:
        model = Project
        fields = ['id', 'address', 'title', 'title_ne',
                  'start_date', 'end_date', 'created_by', 'district']


class ProjectDetailSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    donor = DonaterSerializer()

    class Meta:
        model = Project
        fields = ['id', 'address', 'donor', 'created_at', 'updated_at', 'title', 'title_ne',
                  'budget', 'budget_ne', 'start_date', 'end_date', 'created_by', 'updated_by', 'district']


class TrainingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'address', 'title', 'title_ne',
                  'startDate', 'endDate']


class TrainingSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()
    municipality = MunicipalityySerializer()
    district = DistrictSerializer()

    class Meta:
        model = Training
        fields = '__all__'


class TrainingAnalyticsSerializer(serializers.Serializer):
    total_count = serializers.SerializerMethodField()
    today = serializers.SerializerMethodField()
    total_ongoing = serializers.SerializerMethodField()
    total_complete = serializers.SerializerMethodField()
    municipality_covered = serializers.SerializerMethodField()

    def get_total_count(self, obj):
        return Training.objects.count()

    def get_today(self, obj):
        return date.today()

    def get_total_ongoing(self, obj):
        today = date.today()
        return Training.objects.filter(endDate__lt=today).count()

    def get_total_complete(self, obj):
        today = date.today()
        return Training.objects.filter(endDate__gt=today).count()

    def get_municipality_covered(self, obj):
        return Training.objects.exclude(municipality__isnull=True).count()


class fiscalserializer(serializers.ModelSerializer):
    class Meta:
        model = fiscal
        fields = '__all__'


class GeoHazardAssessmentSerializer(serializers.ModelSerializer):
    fiscal_year = fiscalserializer()

    class Meta:
        model = GeoHazardAssessment
        fields = '__all__'
