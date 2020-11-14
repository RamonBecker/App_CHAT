from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.routing import websocket_urlpatterns #importando da APP

#Configurando a app para receber as rotas do websocket
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
                websocket_urlpatterns
        )
    ),
})
