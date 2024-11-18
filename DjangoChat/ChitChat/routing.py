from django.urls import path, include, re_path
from ChitChat.consumer import ChatConsumer

#
websocket_urlpatterns = [
    re_path(r'ws/chat/$', ChatConsumer.as_asgi()),  # The URL for WebSocket connection
]
