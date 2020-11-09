from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import web_socket_urlpatterns #importando da APP

#Configurando a app para receber as rotas do websocket
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            web_socket_urlpatterns
        )
    ),
})
