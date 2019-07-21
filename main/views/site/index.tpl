{{
from yatl.helpers import *
from ron.widgets import Breadcrumbs
from ron.helpers import URL
}}

{{extend layout}}

{{=H2(name)}}

{{=H3('Breadcrumb test')}}

{{=Breadcrumbs({
    'items':[
        {'label': 'Home', 'url':URL()},
        {'label': 'Services', 'url':URL('services')},
        {'label': 'Contact', 'url':URL('contact')},
    ],
    'item_options':{
        '_class': 'breadcrumb-item'
    }
})}}