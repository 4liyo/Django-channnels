from .consumers import myConsumer
from django.urls import path

ws_urlpatterns = [
    path("ws/some_url/", myConsumer.as_asgi())
]