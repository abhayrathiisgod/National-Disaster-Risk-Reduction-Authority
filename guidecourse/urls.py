from django.urls import path
from guidecourse.views import GuideCourseView, GuideCourseDetailView, CourseListView, CourseInstance, GuideListView

urlpatterns = [
    path('guide/', GuideListView.as_view(), name='guide-courses-list'),
    path('guide/<int:pk>/', GuideCourseDetailView.as_view(),
         name='guide-courses-detail'),
    path('course/', CourseListView.as_view()),
    path('course/<int:pk>/', CourseInstance.as_view()),
]
