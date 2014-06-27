# -*- coding: utf-8 -*-


import sae
from create_app import app

application = sae.create_wsgi_app(app)
