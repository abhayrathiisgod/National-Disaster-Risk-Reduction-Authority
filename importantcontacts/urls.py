from django.urls import path
from importantcontacts.views import ProvinceWiseFocalPersonContactListView, DeocHeadView, LocalDisasterManagementContactView, MohaSubordinateView, MohaPhoneDirectoryView


urlpatterns = [
    path('provincewisefocalcontact/',
         ProvinceWiseFocalPersonContactListView.as_view()),
    path('deocheadcontact/', DeocHeadView.as_view()),
    path('localdisastermanagementcontact',
         LocalDisasterManagementContactView.as_view()),
    path('mohasubordinate/', MohaSubordinateView.as_view()),
    path('mohaphonedirectory/', MohaPhoneDirectoryView.as_view()),
]
