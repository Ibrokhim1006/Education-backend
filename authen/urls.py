""" Django Libraries """
from django.urls import path
from authen.views import (
    UserGroupsViews,
    UserRegisterViews,
    UserSigInViews,
    CheckSmsCode,
    UserProfilesViews,
    UserUpdateView,
    UserTeachersViews,
    UserStudentViews,
)

urlpatterns = [
    path('user_groups_views/', UserGroupsViews.as_view()),
    path('user_register_views/', UserRegisterViews.as_view()),
    path('user_sig_in_views/', UserSigInViews.as_view()),
    path('check_sms_code/', CheckSmsCode.as_view()),
    path('user_profiles_views/', UserProfilesViews.as_view()),
    path('user_update_view/', UserUpdateView.as_view()),
    path('user_teachers_views', UserTeachersViews.as_view()),
    path('user_student_views/', UserStudentViews.as_view()),

]
