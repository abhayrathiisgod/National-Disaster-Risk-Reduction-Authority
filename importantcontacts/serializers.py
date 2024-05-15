from rest_framework import serializers
from importantcontacts.models import ProvinceWiseFocalPersonContactList, DeocHeadList, LocalDisasterManagementContactList, MohaSubordinateList, MohaPhoneDirectoryList, SnakeBites, EmergencyVehicle
from federal.serializers import DistrictSerializer, ProvinceSerializer, MunicipalitySerializer, WardSerializer


class ProvinceWiseFocalPersonContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvinceWiseFocalPersonContactList
        fields = '__all__'


class DeocHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeocHeadList
        fields = '__all__'


class LocalDisasterManagementContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalDisasterManagementContactList
        fields = '__all__'


class MohaSubordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MohaSubordinateList
        fields = '__all__'


class MohaPhoneDirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MohaPhoneDirectoryList
        fields = '__all__'


class SnakeBiteSerializer(serializers.ModelSerializer):
    # district = DistrictSerializer()

    class Meta:
        model = SnakeBites
        fields = ['id', 'treatment_centre', 'treatment_centre_ne', 'district']


class EmergencyVehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmergencyVehicle
        fields = ['id', 'vehicle_type', 'ownership', 'ownership_ne', 'vechicle_no', 'vechicle_no_ne', 'driver_name',
                  'driver_name_ne', 'contact', 'alt_contact', 'condition', 'province', 'district', 'municipality']
