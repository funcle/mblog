# -*- coding: utf-8 -*-

from flask import render_template, Blueprint

photos_router = Blueprint('photos', __name__)

@photos_router.route('')
def index():
    ''''''
    return render_template('/photos/index.html')
