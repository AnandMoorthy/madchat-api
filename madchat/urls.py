from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api-token-auth/', obtain_jwt_token),
    url(r'^api/', include('chat.urls', namespace='chat')),
]
