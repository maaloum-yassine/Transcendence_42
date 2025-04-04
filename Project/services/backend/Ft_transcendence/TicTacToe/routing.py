from django.urls import re_path
from .consumers import TicTacToeConsumer

websocket_urlpatterns = [
    re_path(r'ws/tictactoe/(?P<room_name>\w+)/$', TicTacToeConsumer.as_asgi()),
]
