from django.shortcuts import render
from pressnotenews.models import NewsInfo, PressNote
from rest_framework import generics
from pressnotenews.serializers import ALLNewsInfoSerializer, SpecificNewsInfoSerializer, PressNoteSerializer
# Create your views here.


class NewsInfoViewsetList(generics.ListAPIView):
    queryset = NewsInfo.objects.all()
    serializer_class = ALLNewsInfoSerializer


class NewsInfoViewsetInstance(generics.ListAPIView):
    serializer_class = SpecificNewsInfoSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = NewsInfo.objects.filter(id=pk)
        return queryset


class PressNoteListAPIView(generics.ListAPIView):
    queryset = PressNote.objects.all()
    serializer_class = PressNoteSerializer
