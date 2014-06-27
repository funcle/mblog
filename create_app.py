# -*- coding: utf-8 -*-

import os

from flask import Flask
from apps.urls import routers
from init_app import init_app

current_path = os.path.dirname(__file__)
configfile = os.path.join(current_path, "config.py")

_app = Flask(__name__)

app = init_app(_app, configfile, routers)
