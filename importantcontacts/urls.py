from django.urls import path
from .views import (
    ProvinceWiseFocalPersonContactViewSet,
    DeocHeadViewSet,
    LocalDisasterManagementContactViewSet,
    MohaSubordinateViewSet,
    MohaPhoneDirectoryViewSet,
    SnakeBitesViewSet,
    EmergencyVehicleViewSet,
)

urlpatterns = [
    path('provincewisefocalcontact/', ProvinceWiseFocalPersonContactViewSet.as_view(
        {'get': 'list'}), name='provincewisefocalcontact-list'),
    path('provincewisefocalcontact/<int:pk>/', ProvinceWiseFocalPersonContactViewSet.as_view(
        {'get': 'retrieve'}), name='provincewisefocalcontact-detail'),
    path('deocheadcontact/', DeocHeadViewSet.as_view(
        {'get': 'list'}), name='deocheadcontact-list'),
    path('deocheadcontact/<int:pk>/', DeocHeadViewSet.as_view(
        {'get': 'retrieve'}), name='deocheadcontact-detail'),
    path('localdisastermanagementcontact/', LocalDisasterManagementContactViewSet.as_view(
        {'get': 'list'}), name='localdisastermanagementcontact-list'),
    path('localdisastermanagementcontact/<int:pk>/', LocalDisasterManagementContactViewSet.as_view(
        {'get': 'retrieve'}), name='localdisastermanagementcontact-detail'),
    path('mohasubordinate/', MohaSubordinateViewSet.as_view(
        {'get': 'list'}), name='mohasubordinate-list'),
    path('mohasubordinate/<int:pk>/', MohaSubordinateViewSet.as_view(
        {'get': 'retrieve'}), name='mohasubordinate-detail'),
    path('mohaphonedirectory/', MohaPhoneDirectoryViewSet.as_view(
        {'get': 'list'}), name='mohaphonedirectory-list'),
    path('mohaphonedirectory/<int:pk>/', MohaPhoneDirectoryViewSet.as_view(
        {'get': 'retrieve'}), name='mohaphonedirectory-detail'),
    path('snakebite/', SnakeBitesViewSet.as_view(
        {'get': 'list'}), name='snakebite-list'),
    path('snakebite/<int:pk>/', SnakeBitesViewSet.as_view(
        {'get': 'retrieve'}), name='snakebite-detail'),
    path('EmergencyVehicle/', EmergencyVehicleViewSet.as_view(
        {'get': 'list'}), name='emergency-vehicle-list'),
    path('EmergencyVehicleViewSet/<int:pk>/', EmergencyVehicleViewSet.as_view(
        {'get': 'retrieve'}), name='emergency-vehicle-detail'),
]
