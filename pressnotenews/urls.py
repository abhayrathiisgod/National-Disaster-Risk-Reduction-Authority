from django.urls import path
from pressnotenews.views import NewsInfoViewSet, PressNoteAPIView

urlpatterns = [
    path('newsinfo/', NewsInfoViewSet.as_view({'get': 'list'})),
    path('newsinfo/<slug:slug>/',
         NewsInfoViewSet.as_view({'get': 'retrieve'})),
    path('press-note/', PressNoteAPIView.as_view({'get': 'list'})),
    path('press-note/<slug:slug>/',
         PressNoteAPIView.as_view({'get': 'retrieve'})),
]
