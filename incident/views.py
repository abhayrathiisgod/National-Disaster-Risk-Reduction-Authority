from rest_framework import viewsets
from rest_framework.response import Response
from .models import Loss, Incident
from .serializers import LossSerializer, IncidentSerializer
from django.shortcuts import get_object_or_404


class LossViewSet(viewsets.ModelViewSet):
    queryset = Loss.objects.all()
    serializer_class = LossSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        incident = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(incident)
        return Response(serializer.data)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
