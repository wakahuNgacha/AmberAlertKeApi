from django.urls import path
from .views import ReportView

urlpatterns = [
    path('reports/', ReportView.as_view()),  # List and create
    path('reports/<int:pk>/', ReportView.as_view()),  # Retrieve, update, delete
]
