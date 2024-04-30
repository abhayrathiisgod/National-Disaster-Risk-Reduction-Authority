from django.shortcuts import render
from hazard.models import Hazards
from hazard.serializers import HazardSerializer
from rest_framework import generics

# Create your views here.


class HazardList(generics.ListAPIView):
    queryset = Hazards.objects.all()
    serializer_class = HazardSerializer


class HazardInstance(generics.RetrieveAPIView):
    queryset = Hazards.objects.all()
    serializer_class = HazardSerializer
    lookup_field = 'pk'
