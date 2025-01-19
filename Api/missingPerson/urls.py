from django.urls import path
from .views import MissingPersonView

urlpatterns = [
    path('missing-persons/', MissingPersonView.as_view()),  # List and create
    path('missing-persons/<int:pk>/', MissingPersonView.as_view()),  # Retrieve, update, delete
]