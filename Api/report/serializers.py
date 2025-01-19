from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'  # Use '__all__' to include all fields or specify a list of fields explicitly.
        depth = 1  # This will include related data for `user` and `missingPerson` models.
