#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


from ron import debug, run, Application

from config import config

__version__ = '0.1'

if __name__ == '__main__':
    debug(True)

    app = Application(config)

    app.initialize()

    app = app.get_with_middleware()

    port = int(os.environ.get("PORT", 8080))
    run(app, reloader=True, host='127.0.0.1', port=port)
