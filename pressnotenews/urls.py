from django.urls import path
from pressnotenews.views import NewsInfoViewSet, PressNoteAPIView

urlpatterns = [
    path('newsinfo/', NewsInfoViewSet.as_view({'get': 'list'})),
    path('newsinfo/<int:pk>/',
         NewsInfoViewSet.as_view({'get': 'retrieve'})),
    path('press-note/', PressNoteAPIView.as_view({'get': 'list'})),
    path('press-note/<int:pk>/',
         PressNoteAPIView.as_view({'get': 'retrieve'})),
]
