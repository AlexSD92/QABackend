from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('questions.urls')),
    # path('api-auth/register/', include('dj_rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('api-token-auth/', views.obtain_auth_token),

    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
