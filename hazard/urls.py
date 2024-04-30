from django.urls import path
from hazard.views import HazardList, HazardInstance

urlpatterns = [
    path('hazard/', HazardList.as_view()),
    path('hazard/<int:pk>', HazardInstance.as_view()),
]
