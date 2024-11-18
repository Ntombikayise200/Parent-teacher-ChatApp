# project/asgi.py (replace "project" with your actual project name)

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from ChitChat.routing import websocket_urlpatterns  # Import the routing from chat app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoChat.settings')  # Replace with your project name

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # This stack handles WebSocket connections and user authentication
        URLRouter(
            websocket_urlpatterns  # Adding WebSocket URLs here
        )
    ),
})
