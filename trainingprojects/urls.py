from django.urls import path
from .views import ProjectListView, TrainingAnalyticView, TrainingView

urlpatterns = [
    path('projects/', ProjectListView.as_view({'get': 'list'})),
    path('projects/<int:pk>/',  ProjectListView.as_view({'get': 'retrieve'})),
    path('trainings/', TrainingView.as_view({'get': 'list'})),
    path('trainings/<int:pk>/', TrainingView.as_view({'get': 'retreive'})),
    path('analytics/', TrainingAnalyticView.as_view()),
]
