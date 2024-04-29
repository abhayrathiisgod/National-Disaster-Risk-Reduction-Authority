from django.urls import path
from .views import ProjectInstance, ProjectListView

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('projects/<int:pk>/', ProjectInstance.as_view()),
]
