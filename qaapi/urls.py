from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', include('questions.urls')),
    # path('api-auth/register/', include('dj_rest_auth.registration.urls')),
    path('users/', include('users.urls')),
    path('api-token-auth/', views.obtain_auth_token),

    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
