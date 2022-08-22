# TAKEN FROM https://www.codersarts.com/post/how-to-create-register-and-login-api-using-django-rest-framework-and-token-authentication

from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]