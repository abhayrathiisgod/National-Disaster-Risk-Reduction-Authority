from django.urls import path
from hazard.views import HazardAPIview

urlpatterns = [
    path('hazard/',  HazardAPIview.as_view({'get': 'list'})),
    path('hazard/<int:pk>/', HazardAPIview.as_view({'get': 'retrieve'})),
]
