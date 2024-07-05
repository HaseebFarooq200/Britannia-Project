from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenRefreshView
from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.RegisterAPI.as_view()),
    path("login/", views.LoginAPI.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("logout/", views.LogoutAPI.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
