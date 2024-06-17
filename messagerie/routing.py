from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from messagerie.consumers import MessagerieConsumer
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack


websocket_urlpatterns = [
    path("ws/messagerie/<int:id>", MessagerieConsumer.as_asgi()),
]

"""application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        )
    ),
})"""