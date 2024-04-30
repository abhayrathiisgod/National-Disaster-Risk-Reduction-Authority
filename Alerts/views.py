from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import AlertList
from .serializers import AlertListSerializer


class AlertListView(generics.ListAPIView):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer


class AlertInstanceView(generics.ListAPIView):
    queryset = AlertList.objects.all()
    serializer_class = AlertListSerializer
    lookup_field = 'pk'
