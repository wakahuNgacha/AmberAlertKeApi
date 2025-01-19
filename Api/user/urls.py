from django.urls import path
from .views import UserView

urlpatterns = [
    path('users/', UserView.as_view()),  # List and create
    path('users/<int:pk>/', UserView.as_view()),  # Retrieve, update, delete
]
