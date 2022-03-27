from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User_Info


class UserinfoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user_pw'] = make_password(validated_data['user_pw'])# 암호화
        user = User_Info.objects.create(**validated_data)
        return user

    class Meta:
        model = User_Info
        fields =('user_id', 'user_pw', 'username')