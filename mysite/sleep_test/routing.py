from django.urls import path
from sleep_test import consumers

websocket_urlpatterns = [
    path('ws/all/', consumers.StudentConsumer.as_asgi()),
    path('ws/chat/<int:pk>/',consumers.ChatConsumer.as_asgi()),
]