{{

from yatl.helpers import *
from ron.widgets import Breadcrumbs

}}

{{extend '../layout.tpl'}}

USER {{=H1(data)}}

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