from django.urls import path
from .views import LossViewSet, IncidentViewSet

urlpatterns = [
    # path('losses/', LossViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('losses/<int:pk>/', LossViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('incidents/', IncidentViewSet.as_view({'get': 'list'})),
    path('incidents/<int:pk>/', IncidentViewSet.as_view({'get': 'retrieve'})),
]
