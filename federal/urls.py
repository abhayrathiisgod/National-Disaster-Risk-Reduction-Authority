from django.urls import path
from federal.views import ProvinceView, DistrictView, MunicipalityView, WardView

urlpatterns = [
    path('provinces/', ProvinceView.as_view({'get': 'list'})),
    path('provinces/<int:pk>/', ProvinceView.as_view({'get': 'retrieve'})),
    path('districts/', DistrictView.as_view({'get': 'list'})),
    path('districts/<int:pk>/', DistrictView.as_view({'get': 'retrieve'})),
    path('municipalities/', MunicipalityView.as_view({'get': 'list'})),
    path('municipalities/<int:pk>/',
         MunicipalityView.as_view({'get': 'retrieve'})),
    path('wards/', WardView.as_view({'get': 'list'})),
    path('wards/<int:pk>/', WardView.as_view({'get': 'retrieve'})),
]
