from django.urls import path
from . import views

urlpatterns = [
    path(
        'skills/', views.SkillsAPIView.as_view({'get': 'list'}), name='skills-list'),
    path('skills/<int:pk>/',
         views.SkillsAPIView.as_view({'get': 'retrieve'}), name='skills-detail'),

    path('designation/', views.DesignationAPIView.as_view({'get': 'list'}),
         name='designation-list'),
    path('designation/<int:pk>/', views.DesignationAPIView.as_view({'get': 'retrieve'}),
         name='designation-detail'),

    path('department/', views.DepartmentAPIView.as_view({'get': 'list'}),
         name='department-list'),
    path('department/<int:pk>/', views.DepartmentAPIView.as_view({'get': 'retrieve'}),
         name='department-detail'),

    path('trainingorg/', views.TrainingOrgAPIView.as_view({'get': 'list'}),
         name='trainingorg-list'),
    path('trainingorg/<int:pk>/', views.TrainingOrgAPIView.as_view({'get': 'retrieve'}),
         name='trainingorg-detail'),

    path('trainingcertificate/', views.TrainingCertificateAPIView.as_view({'get': 'list'}),
         name='trainingcertificate-list'),
    path('trainingcertificate/<int:pk>/',
         views.TrainingCertificateAPIView.as_view({'get': 'retrieve'}), name='trainingcertificate-detail'),

    path('trainings/',
         views.TrainingsAPIView.as_view({'get': 'list'}), name='trainings-list'),
    path('trainings/<int:pk>/', views.TrainingsAPIView.as_view({'get': 'retrieve'}),
         name='trainings-detail'),

    path('officerprofile/', views.OfficerProfileAPIView.as_view({'get': 'list'}),
         name='officerprofile-list'),
    path('officerprofile/<int:pk>/', views.OfficerProfileAPIView.as_view({'get': 'retrieve'}),
         name='officerprofile-detail'),

    path('commiteprofile/', views.CommiteProfileAPIView.as_view({'get': 'list'}),
         name='commiteprofile-list'),
    path('commiteprofile/<int:pk>/',
         views.CommiteProfileAPIView.as_view({'get': 'retrieve'}), name='commiteprofile-detail'),

    path('nationalcouncilhead/', views.NationalCouncilHeadAPIView.as_view({'get': 'list'}),
         name='nationalcouncilhead-list'),
    path('nationalcouncilhead/<int:pk>/',
         views.NationalCouncilHeadAPIView.as_view({'get': 'retrieve'}), name='nationalcouncilhead-detail'),

    path('executivecommittehead/', views.ExecutiveCommitteHeadAPIView.as_view({'get': 'list'}),
         name='executivecommittehead-list'),
    path('executivecommittehead/<int:pk>/',
         views.ExecutiveCommitteHeadAPIView.as_view({'get': 'retrieve'}), name='executivecommittehead-detail'),

    path('officershead/', views.OfficersHeadAPIView.as_view({'get': 'list'}),
         name='officershead-list'),
    path('officershead/<int:pk>/', views.OfficersHeadAPIView.as_view({'get': 'retrieve'}),
         name='officershead-detail'),

    path('officersspokesperson/', views.OfficersSpokesPersonAPIView.as_view({'get': 'list'}),
         name='officersspokesperson-list'),
    path('officersspokesperson/<int:pk>/',
         views.OfficersSpokesPersonAPIView.as_view({'get': 'retrieve'}), name='officersspokesperson-detail'),

    path('informationofficer/', views.InformationOfficerAPIView.as_view({'get': 'list'}),
         name='informationofficer-list'),
    path('informationofficer/<int:pk>/',
         views.InformationOfficerAPIView.as_view({'get': 'retrieve'}), name='informationofficer-detail'),

    path('councilprofileview/', views.CouncilProfileView.as_view(),
         name='councilprofileview'),
]
