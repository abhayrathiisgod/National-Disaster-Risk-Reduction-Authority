from django.urls import path
from .views import ProjectListView, TrainingAnalyticView, TrainingView, GeoHazardView

urlpatterns = [
    path('projects/', ProjectListView.as_view({'get': 'list'})),
    path('projects/<int:pk>/',  ProjectListView.as_view({'get': 'retrieve'})),
    path('trainings/', TrainingView.as_view({'get': 'list'})),
    path('trainings/<int:pk>/', TrainingView.as_view({'get': 'retrieve'})),
    path('geohazard/', GeoHazardView.as_view({'get': 'list'})),
    path('geohazard/<int:pk>/', GeoHazardView.as_view({'get': 'retrieve'})),
    path('analytics/', TrainingAnalyticView.as_view()),
]
