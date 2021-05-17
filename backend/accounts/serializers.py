from typing import Tuple
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields =('email','username','password','name')
        extra_kwargs = {'password':{'write_only':True,'min_length':8}}

    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type':'password'},
        trim_whitespace = False
    )
    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            email=email,
            password=password
        )
        if not user:
            raise serializers.ValidationError("Invalid User Credentials")
        attrs['user'] =user
        return attrs