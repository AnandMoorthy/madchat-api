from django.conf.urls import url

from .views import UserListView, GroupListView, LoginView, RegisterUserView
from .views import DirectMessageView, GroupMessageView, index, room

urlpatterns = [
    # url(r'^$', index, name='index'),
    # url(r'^(?P<room_name>[^/]+)/$', room, name='room'),
    url(r'^auth/login/?$', LoginView.as_view(), name="user-login"),
    url(r'^auth/register/?$', RegisterUserView.as_view(), name="user-register"),
    url(r'^users/?$', UserListView.as_view(), name="users-all"),
    url(r'^groups/?$', GroupListView.as_view(), name="group-all"),
    url(r'^dm/(?P<pk>\w+)/?$', DirectMessageView.as_view(), name="dm"),
    url(r'^group/(?P<id>\w+)/?$', GroupMessageView.as_view(), name="group"),

]
