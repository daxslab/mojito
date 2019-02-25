{{
from yatl.helpers import *
from ron.widgets import Breadcrumbs
}}

{{extend '../layout.tpl'}}

{{=H2(name)}}

{{=H3('Breadcrumb test')}}

{{=Breadcrumbs({
    'items':[
        {'label': 'Home', 'url':'/'},
        {'label': 'Services', 'url':'/services'},
        {'label': 'Contact', 'url':'/contact'},
    ],
    'item_options':{
        '_class': 'breadcrumb-item'
    }
})}}