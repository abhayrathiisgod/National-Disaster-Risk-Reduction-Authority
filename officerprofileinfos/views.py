from rest_framework import generics
from rest_framework.views import APIView
from .models import Skills, Designation, Department, TrainingOrg, TrainingCertificate, Trainings, OfficerProfile, CommiteProfile, NationalCouncilHead, ExecutiveCommitteHead, OfficersHead, OfficersSpokesPerson, InformationOfficer
from .serializers import SkillsSerializer, DesignationSerializer, DepartmentSerializer, TrainingOrgSerializer, TrainingCertificateSerializer, TrainingsSerializer, OfficerProfileSerializer, CommiteProfileSerializer, NationalCouncilHeadSerializer, ExecutiveCommitteHeadSerializer, OfficersHeadSerializer, OfficersSpokesPersonSerializer, InformationOfficerSerializer
from rest_framework.response import Response


class SkillsListAPIView(generics.ListAPIView):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


class DesignationListAPIView(generics.ListAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class DepartmentListAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class TrainingOrgListAPIView(generics.ListAPIView):
    queryset = TrainingOrg.objects.all()
    serializer_class = TrainingOrgSerializer


class TrainingCertificateListAPIView(generics.ListAPIView):
    queryset = TrainingCertificate.objects.all()
    serializer_class = TrainingCertificateSerializer


class TrainingsListAPIView(generics.ListAPIView):
    queryset = Trainings.objects.all()
    serializer_class = TrainingsSerializer


class OfficerProfileListAPIView(generics.ListAPIView):
    queryset = OfficerProfile.objects.all()
    serializer_class = OfficerProfileSerializer


class CommiteProfileListAPIView(generics.ListAPIView):
    queryset = CommiteProfile.objects.all()
    serializer_class = CommiteProfileSerializer


class NationalCouncilHeadListAPIView(generics.ListAPIView):
    queryset = NationalCouncilHead.objects.all()
    serializer_class = NationalCouncilHeadSerializer


class ExecutiveCommitteHeadListAPIView(generics.ListAPIView):
    queryset = ExecutiveCommitteHead.objects.all()
    serializer_class = ExecutiveCommitteHeadSerializer


class OfficersHeadListAPIView(generics.ListAPIView):
    queryset = OfficersHead.objects.all()
    serializer_class = OfficersHeadSerializer


class OfficersSpokesPersonListAPIView(generics.ListAPIView):
    queryset = OfficersSpokesPerson.objects.all()
    serializer_class = OfficersSpokesPersonSerializer


class InformationOfficerListAPIView(generics.ListAPIView):
    queryset = InformationOfficer.objects.all()
    serializer_class = InformationOfficerSerializer


class OfficerProfileView(generics.RetrieveAPIView):
    queryset = OfficerProfile.objects.all()
    serializer_class = OfficerProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        designation_serializer = DesignationSerializer(
            instance.designation.all(), many=True)

        department_serializer = DepartmentSerializer(
            instance.departments.all(), many=True)
        response_data = {
            "id": instance.id,
            "name": instance.name,
            "name_ne": instance.name_ne,
            "designation": designation_serializer.data,
            "department": department_serializer.data,
            "image": instance.image.url,
            "from_date": instance.from_date,
            "to_date": instance.to_date
        }

        return Response(response_data)


class CouncilProfileView(APIView):
    def get(self, request, *args, **kwargs):

        national_council_head = NationalCouncilHead.objects.first()
        executive_committe_head = ExecutiveCommitteHead.objects.first()
        officers_head = OfficersHead.objects.first()
        officers_spokes_person = OfficersSpokesPerson.objects.all()
        information_officer = InformationOfficer.objects.all()
        national_council_head_serializer = NationalCouncilHeadSerializer(
            national_council_head)
        executive_committe_head_serializer = ExecutiveCommitteHeadSerializer(
            executive_committe_head)
        officers_head_serializer = OfficersHeadSerializer(officers_head)
        officers_spokes_person_serializer = OfficersSpokesPersonSerializer(
            officers_spokes_person, many=True)
        information_officer_serializer = InformationOfficerSerializer(
            information_officer, many=True)

        results = [
            {
                "id": 1,
                "national_council_head": national_council_head_serializer.data,
                "executive_committe_head": executive_committe_head_serializer.data,
                "officers_head": officers_head_serializer.data,
                "officers_spokesperson": officers_spokes_person_serializer.data,
                "information_officer": information_officer_serializer.data,
            }
        ]

        return Response({"results": results})
