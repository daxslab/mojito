# from bottle import Jinja2Template

from main.module import Main
from ron.caching.cache import CacheComponent
from ron.models import PeeweeDB
from ron.web.session import SessionComponent
from user.module import User

config = {

    'components': {
        'cache_manager': {
            'class': CacheComponent,
            'options': {
                'type': 'file',
                'data_dir': './runtime/cache/data',
                'lock_dir': './runtime/cache/lock',
                'expire': 300,
            },
        },
        'session_manager': {
            'class': SessionComponent,
            'on_initialize': True,
            'options': {
                'type': 'file',
                'cookie_expires': 300,
                'data_dir': './runtime/session',
                'auto': True,
            }
        },
        'db': {
            'class': PeeweeDB,
            'on_initialize': True,
            'options': {
                'connection': 'sqlite:///:memory:'
            }
        }
    },

    # 'middlewares': [
    #     {
    #         'class': SessionMiddleware,
    #         'options': {
    #             'session.type': 'file',
    #             'session.cookie_expires': 300,
    #             'session.data_dir': './runtime/session',
    #             'session.auto': True
    #         }
    #     }
    # ],

    'modules': {
        'main': {
            'class': Main,
            'options': {
                'mount_type': 'merge',
                # 'template_adapter': Jinja2Template,
            },
        },
        'user': {
            'class': User,
            'options': {
                # 'views_path': os.path.dirname(os.path.abspath(__file__)) + '/main/views',
                # 'template_adapter': Jinja2Template,
            }
        }
    },
}
