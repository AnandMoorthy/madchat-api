from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Groups, DirectMessages, GroupMembers, GroupMessages


class UserSerializer(serializers.ModelSerializer):
    '''
    This serializer serialize user data
    '''
    class Meta:
        model = User
        fields = ("username", "email", "id")


class GroupSerializer(serializers.ModelSerializer):
    '''
    This serializer serialize group data
    '''
    class Meta:
        model = Groups
        fields = ("id", "name")


class GroupMembersSerializer(serializers.ModelSerializer):
    '''
    This serializer serialize group member data
    '''
    class Meta:
        model = GroupMembers
        fields = ("id", "user")


class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token
    """
    token = serializers.CharField(max_length=255)


class DirectMessageSerializer(serializers.ModelSerializer):
    '''
    This serializer serialize user data
    '''
    class Meta:
        model = DirectMessages
        fields = ("from_user", "to_user", "message", "added_on")


class GroupMessageSerializer(serializers.ModelSerializer):
    '''
    This serializer serialize group message data
    '''
    class Meta:
        model = GroupMessages
        fields = ("user", "message", "added_on")


# class DirectMessageDetailsSerialzier(serializers.ModelSerializer):
#     dm =
#     class Meta:
#         model = DirectMessages
#         fields = ("from_user", "to_user", "message", "added_on")
