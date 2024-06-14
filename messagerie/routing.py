from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/messagerie/', MessagerieConsumer.as_asgi()),
]