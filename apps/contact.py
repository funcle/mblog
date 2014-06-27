# -*- coding: utf-8 -*-

from flask import render_template, Blueprint

contact_router = Blueprint('contact', __name__)

@contact_router.route('')
def index():
    '''联系我'''
    return render_template('/contact/index.html')
    