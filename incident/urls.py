from django.urls import path
from .views import LossViewSet, IncidentInstanceSet, IncidentViewSet

urlpatterns = [
    # path('losses/', LossViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('losses/<int:pk>/', LossViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path('incidents/', IncidentViewSet.as_view()),
    path('incidents/<int:pk>/', IncidentInstanceSet.as_view()),
]
