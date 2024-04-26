from django.shortcuts import render
from rest_framework import generics
from officerprofileinfos.models import Officer, Designation
from officerprofileinfos.serializers import OfficerSerializer, DesignationSerializer
from officerprofileinfos.pagination import PaginationClass
# Create your views here.


# councilcommitieview
class CouncilCommittieView(generics.ListAPIView):
    queryset = Designation.objects.filter(is_executive_committee=True)
    serializer_class = OfficerSerializer
    pagination_class = PaginationClass
