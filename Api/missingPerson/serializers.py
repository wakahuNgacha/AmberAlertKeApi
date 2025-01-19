from rest_framework import serializers
from .models import MissingPerson

class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = '__all__'  # You can specify individual fields instead of using '__all__'
