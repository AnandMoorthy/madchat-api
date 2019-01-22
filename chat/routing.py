from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/api/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
