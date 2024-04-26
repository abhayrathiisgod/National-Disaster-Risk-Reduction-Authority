from django.urls import path
from officerprofileinfos.views import CouncilCommittieView

urlpatterns = [
    path('councilcommitteeprofile/', CouncilCommittieView.as_view()),
]
