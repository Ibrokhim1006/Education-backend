""" Django Libraries """
from django.urls import path
from authen.views import UserProfilesViews

urlpatterns = [
    path(
        'user_profiles_views/',
        UserProfilesViews.as_view(),
    ),

]
