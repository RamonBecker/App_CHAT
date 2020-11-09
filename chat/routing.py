from django.urls import re_path
from .consumers import ChatConsumer

web_socket_urlpatterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+/$)', ChatConsumer), #Rota específica do channels
    # ws = websocket  | Expressão regular

]