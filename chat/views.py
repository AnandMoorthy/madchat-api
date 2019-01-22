import json

from django.shortcuts import render
from django.utils.safestring import mark_safe

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import status
from rest_framework.response import Response

from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer, TokenSerializer
from .serializers import DirectMessageSerializer, GroupMessageSerializer
from rest_framework import permissions

from .models import Groups, DirectMessages, GroupMessages, GroupMembers
# from .models import DirectMessages, GroupMembers, GroupMessages,

# Get the JWT settings, add these lines after the import/from lines
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


class RegisterUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        '''
        This module will register a user with the input of username and
        password
        '''
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "Fields Missing"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        '''
        This module will login the user and return the JWT Token
        '''
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(
                data={
                    "token": jwt_encode_handler(
                        jwt_payload_handler(user)
                    )
                }
            )
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserListView(generics.ListAPIView):
    '''
    List all the users
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class GroupListView(generics.ListAPIView):
    '''
    List all the groups
    '''
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticated,)


# class GroupMembersListView(generics.ListAPIView):
#     queryset = GroupMembers.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = (permissions.IsAuthenticated,)


class DirectMessageView(generics.ListAPIView):

    queryset = DirectMessages.objects.all()
    serializer_class = DirectMessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
        GET Direct messsages between two users by user pk
        '''
        try:
            dm = self.queryset.filter(
                to_user__in=[kwargs["pk"], request.user.id],
                from_user__in=[kwargs["pk"], request.user.id]
            )
            return Response(DirectMessageSerializer(dm, many=True).data)
        except DirectMessages.DoesNotExist:
            return Response(
                data={
                    "message": "No Message Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )


class GroupMessageView(generics.ListAPIView):

    queryset = GroupMessages.objects.all()
    serializer_class = GroupMessageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        '''
        GET Group messages by group id
        '''
        try:
            group_messages = self.queryset.filter(group=kwargs["id"])
            return Response(GroupMessageSerializer(
                group_messages, many=True).data
            )
        except GroupMessages.DoesNotExist:
            return Response(
                data={
                    "message": "No Message Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
