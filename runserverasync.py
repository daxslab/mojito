#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from gevent import monkey; monkey.patch_all()

from ron import debug, run, Application

from config import config

__version__ = '0.1'

if __name__ == '__main__':
    debug(True)

    app = Application(config)

    app.initialize()

    app = app.get_with_middleware()

    port = int(os.environ.get("PORT", 8080))
    run(app, reloader=True, host='0.0.0.0', port=port, server='gevent')
