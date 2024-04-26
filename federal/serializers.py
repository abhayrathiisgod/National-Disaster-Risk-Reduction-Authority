from rest_framework import serializers
from .models import Province, District, Municipality, Ward


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ['id', 'province_name', 'province_name_ne', 'code']


class DistrictSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()  # Correct field name

    class Meta:
        model = District
        fields = ['id', 'district_name', 'district_name_ne',
                  'code', 'province']  # Correct field name


class MunicipalitySerializer(serializers.ModelSerializer):
    province = ProvinceSerializer(read_only=True)  # Correct field name
    district = DistrictSerializer(read_only=True)  # Correct field name

    class Meta:
        model = Municipality
        fields = ['id', 'municipality_name', 'municipality_name_ne',
                  'code', 'province', 'district']  # Correct field names


class WardSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()  # Correct field name
    district = DistrictSerializer()  # Correct field name
    municipality = MunicipalitySerializer()  # Correct field name

    class Meta:
        model = Ward
        fields = ['id', 'ward_name', 'ward_name_ne', 'province',
                  'district', 'municipality']  # Correct field names
