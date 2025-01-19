from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # You can replace '__all__' with a list of fields, e.g., ['firstName', 'secondName', ...]
