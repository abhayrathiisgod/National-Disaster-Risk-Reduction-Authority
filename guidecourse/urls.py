from django.urls import path
from guidecourse.views import GuideCourseView, CourseView, GuideListView

urlpatterns = [
    path(
        'guide/', GuideListView.as_view(), name='guide-courses-list'),
    path('guide/<int:pk>/', GuideCourseView.as_view({'get': 'retrieve'}),
         name='guide-courses-detail'),
    path('course/', CourseView.as_view({'get': 'list'})),
    path('course/<int:pk>/', CourseView.as_view({'get': 'retrieve'})),
]
