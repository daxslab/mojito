# from bottle import Jinja2Template

from main.module import Main
# from ron.base.view import View
from ron.caching.cache import CacheComponent
from ron.models import PeeweeDB
from ron.web.session import SessionComponent
from ron.web.urlmanager import UrlManagerComponent
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
                'connection': 'sqlite:///test.db'
            }
        },
        'url_manager': {
            'class': UrlManagerComponent,
            'options': {
                'rules': [
                    ('/config_route', 'GET', 'main.controllers.site.config_route'),
                    ('/redefined_route', 'GET', 'main.controllers.site.config_redefined_route'),
                ],
                'remove_rules': [
                    ('/redefined', '*'),
                    # ('/redefined', 'GET'),
                    # ('/redefined', ['GET', 'POST']),
                ]
            }
        }
        # 'view': {
        #     'class': View,
        #     'options': {
        #         'layout': 'views/layout.tpl',
        #     }
        # }
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
                'mount_type': 'merge'
            },
        },
        'user': {
            'class': User,
            'options': {
                # 'components': {
                #     'view': {
                #         'class': View,
                #         'options': {
                #             # 'template_adapter': Jinja2Template,
                #             'path': 'views'
                #         }
                #     }
                # }
            },

        }
    },
}
