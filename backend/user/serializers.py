from django.core.exceptions import ValidationError

from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


##################### TODO : Authentication #####################


class LoginSerializer(TokenObtainPairSerializer):
    
     @classmethod
     def get_token(cls, user):
        token = super().get_token(user)

        token['phone'] = user.phone
        token['email'] = user.email
        token['username'] = user.username
        token['full_name'] = user.full_name
        
        try:
            token['vendor_id'] = user.vendor.id
        except:
            token['vendor_id'] = 0
        
        return token 
        

class RegisterSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = User 
        fields = ['phone', 'email', 'username', 'full_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(message='')
        return attrs
    
    def create(self, validated_data):
        return super().create(validated_data)
