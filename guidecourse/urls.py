from django.urls import path
from guidecourse.views import GuideCourseView, GuideCourseDetailView

urlpatterns = [
    path('guide-courses/', GuideCourseView.as_view(), name='guide-courses-list'),
    path('guide-courses/<str:name>/', GuideCourseDetailView.as_view(),
         name='guide-courses-detail'),
]
