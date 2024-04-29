from django.urls import path
from importantcontacts.views import ProvinceWiseFocalPersonContactListView, DeocHeadView, LocalDisasterManagementContactView, MohaSubordinateView, MohaPhoneDirectoryView, SnakeBitesView, AmbulanceView, FireTruckView


urlpatterns = [
    path('provincewisefocalcontact/',
         ProvinceWiseFocalPersonContactListView.as_view()),
    path('deocheadcontact/', DeocHeadView.as_view()),
    path('localdisastermanagementcontact',
         LocalDisasterManagementContactView.as_view()),
    path('mohasubordinate/', MohaSubordinateView.as_view()),
    path('mohaphonedirectory/', MohaPhoneDirectoryView.as_view()),
    path('snakebite/', SnakeBitesView.as_view()),
    path('ambulance/', AmbulanceView.as_view()),
    path('firetruck/', FireTruckView.as_view()),

]
