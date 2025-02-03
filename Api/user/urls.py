from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserView, UserRegistrationView

urlpatterns = [
        # Registration endpoint
    path('register/', UserRegistrationView.as_view(), name='register'),
    
    # JWT endpoints for login and token refresh
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserView.as_view()),  # List and create
    path('users/<int:pk>/', UserView.as_view()),  # Retrieve, update, delete
]
