from firetut import handlers
from firenado import tornadoweb


class FiretutComponent(tornadoweb.TornadoComponent):

    def get_handlers(self):
        return [
            (r"/", handlers.IndexHandler),
            (r"/login", handlers.LoginHandler),
        ]    