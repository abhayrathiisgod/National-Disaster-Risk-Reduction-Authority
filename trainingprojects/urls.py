from django.urls import path
from .views import ProjectInstance, ProjectListView, TrainingAnalyticView, TrainingView

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('projects/<int:pk>/', ProjectInstance.as_view()),
    path('trainings/', TrainingView.as_view()),
    path('analytics/', TrainingAnalyticView.as_view()),
]
