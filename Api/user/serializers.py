from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # You can replace '__all__' with a list of fields, e.g., ['firstName', 'secondName', ...]

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'firstName', 'secondName', 'surname', 'location', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match!")
        return data

    def create(self, validated_data):
        # Remove the password_confirm field
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        # Create the user instance
        user = User(**validated_data)
        user.set_password(password)  # This hashes the password
        user.save()
        return user
