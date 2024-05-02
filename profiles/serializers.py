from rest_framework import serializers
from profiles.models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead, OfficersHead, OfficersSpokesPerson, InformationOfficer


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TrainingOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingOrg
        fields = '__all__'


class TrainingCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCertificate
        fields = '__all__'


class TrainingsSerializer(serializers.ModelSerializer):
    training_org = TrainingOrgSerializer()
    training_certificate = TrainingCertificateSerializer(many=True)

    class Meta:
        model = Trainings
        fields = ['id', 'training_org', 'training_certificate', 'title',
                  'title_ne', 'description', 'description_ne', 'start_date', 'end_date']


class OfficerProfileSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()
    departments = DepartmentSerializer(many=True)
    skills = SkillsSerializer(many=True)
    trainings = TrainingsSerializer(many=True)

    class Meta:
        model = OfficerProfile
        fields = ['id', 'designation', 'departments', 'skills', 'trainings', 'name', 'name_ne', 'mobile',
                  'email', 'additional_info', 'additional_info_ne', 'image', 'from_date', 'to_date', 'order']


class OfficerProfileforalertSerializer(serializers.Serializer):
    class Meta:
        model = OfficerProfile
        fields = ['designation', 'name', 'name_ne', 'mobile',
                  'email', 'additional_info', 'additional_info_ne']


class CommiteProfileSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()

    class Meta:
        model = CommiteProfile
        fields = ['id', 'designation', 'name', 'name_ne',
                  'additional_info', 'additional_info_ne', 'image', 'order']


class NationalCouncilHeadSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()

    class Meta:
        model = NationalCouncilHead
        fields = '__all__'


class ExecutiveCommitteHeadSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()

    class Meta:
        model = ExecutiveCommitteHead
        fields = '__all__'


class OfficersHeadSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()

    class Meta:
        model = OfficersHead
        fields = '__all__'


class OfficersSpokesPersonSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()

    class Meta:
        model = OfficersSpokesPerson
        fields = '__all__'


class InformationOfficerSerializer(serializers.ModelSerializer):
    designation = DesignationSerializer()

    class Meta:
        model = InformationOfficer
        fields = '__all__'
