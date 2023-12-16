from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, Profile


class UserLoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields =['id', 'phone', 'email', 'password', 'first_name', 'last_name', 'zipcode', 'address']
        labels = {
            'password': 'گذر واژه',
        }
    
    def create(self, **validated_data):
        return super().create(validated_data)
