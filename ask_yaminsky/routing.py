from channels.routing import route
from ask.consumers import ws_connect, ws_disconnect


channel_routing = [
    route('websocket.connect', ws_connect, path=r'^/answers/(?P<pk>[0-9]+)/$'),
    route('websocket.disconnect', ws_disconnect, path=r'^/answers/(?P<pk>[0-9]+)/$'),
]