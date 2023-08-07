from django.contrib import admin
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from djoser.views import UserViewSet
from customuser.reset_password_view import custom_password_reset_confirm
from customuser.email_verification_view import email_verification

urlpatterns = [
    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Password Reset View (Djoser's default view for requesting a password reset)
    path('/', include('djoser.urls')),

    # Register a New User (Djoser's default view for user registration)
    path('register/', UserViewSet.as_view(actions={'post': 'create'}), name='user-create'),

    # Djoser's Authentication URLs (login, logout, and other authentication-related endpoints)
    path('auth/', include('djoser.urls.authtoken')),

    # Drf-spectacular endpoint for generating the OpenAPI schema
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Optional UI for the OpenAPI schema (Swagger UI)
    path('api/docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Custom view for confirming password reset
    path('password/reset/confirm/<uidb64>/<token>/', custom_password_reset_confirm,
         name='custom_password_reset_confirm'),

    # Custom view for email verification
    path('activate/<str:uidb64>/<str:token>/', email_verification, name='email_verification'),

    # View for the password reset complete page
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Optional UI for the OpenAPI schema (ReDoc)
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
