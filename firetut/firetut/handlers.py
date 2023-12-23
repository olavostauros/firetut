from firenado import tornadoweb


class IndexHandler(tornadoweb.TornadoHandler):

    def get(self):
        page_name = "doo bee doo bee doo"
        self.render("index.html", page_name=page_name)


class LoginHandler(tornadoweb.TornadoHandler):

    def get(self):
        page_name = "Login"
        self.render("login.html", page_name=page_name)