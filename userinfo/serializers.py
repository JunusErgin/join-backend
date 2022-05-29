from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    # class Meta:
    #     model = User
    #     fields = ['id', 'email','first_name', 'last_name', ] 

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Profile
        fields = ['id', 'group', 'user',]