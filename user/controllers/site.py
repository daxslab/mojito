from ron.web import Controller
# from ron.web.actions import action


class Site(Controller):

    # @Controller.action('/<name>', ext='.html')
    @Controller.action('/')
    def index(self):
        return dict(
            data='Hello World'
        )

    @Controller.action('/<name>')
    def param(self, name):
        return dict(
            name=name
        )
