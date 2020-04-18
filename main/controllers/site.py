from time import sleep

from main.models.person import Person
from ron.web import Controller

from ron import Application

# Application is a singleton
app = Application()

class Site(Controller):

    # @a.cache_manager.cache(expire=3600)
    # this is an example using the basic route decorator and defining
    # a view using the view decorator
    @Controller.route('/')
    @Controller.route('/index') # we can use more than one route
    @Controller.view('site/index.tpl') # relative path from module views folder (an absolute path to template can also be used)
    def index(self):
        return dict(name='index')

    # this is an example using the action route decorator, this will
    # find by default a view template with the function name
    @Controller.action('/action')
    def route_action(self):
        return dict(name='action')

    # using a param in a url
    @Controller.action('/url_param/<value>')
    def url_param(self, value):
        return dict(name='url_param', value=value)

    # controller+view caching example using the defined cache_manager component
    @app.cache_manager.cache()
    @Controller.action('/views_caching')
    def views_caching(self):
        print('Cache miss')
        return dict(name='views_caching')

    # data caching
    @Controller.action('/data_caching')
    def data_caching(self):
        data_cache = app.cache_manager.get_cache('my_data')
        try:
            data = data_cache.get('data')
        except KeyError:
            data = None
        if not data:
            sleep(5)
            text = 'this request was slow because there is no cache'
            data_cache.put('data', 'this text was cached')
        else:
            text = 'this request was fast because the information was cached'

        return dict(name='views_caching', text=text, cached_data=data)

    # session example using the defined session_manager component
    @Controller.route('/session')
    def session(self):
        session = app.session_manager()
        session['test'] = session.get('test', 0) + 1
        session.save()
        return dict(status='ok', data={'count':session['test']})

    # Peewee ORM
    @Controller.route('/persons', method='GET')
    def persons(self):
        huey = Person(name='huey')
        huey.save()
        result = Person.select().dicts()
        return dict(status='ok', data=list(result))

    # This example can explore the gevent async capabilities. In a not gevent based application
    # the sleep() function will block the application thread, instead, a gevent based application
    # will handle thousands of concurrent requests
    @Controller.route('/stream')
    def stream(self):
        yield 'START'
        sleep(3)
        yield 'MIDDLE'
        sleep(5)
        yield 'END'
