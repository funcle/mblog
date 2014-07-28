# -*- coding: utf-8 -*-

import os
import time
import datetime
import logging

from flask import Flask, session, request, flash, \
    redirect, jsonify, url_for, render_template, current_app

from extensions import db

def init_app(app, config, urls):
    
    app.config.from_pyfile(config)
    configure_extensions(app)
    configure_blueprints(app, urls)
    configure_template_filters(app)
    configure_context_processors(app)

    return app

def configure_extensions(app):
    '''configure extensions'''
    db.init_app(app)

def configure_blueprints(app, urls):
    
    for blueprints, url_prefix in urls:
        app.register_blueprint(blueprints, url_prefix=url_prefix)

def configure_template_filters(app):
    
    @app.template_filter()
    def content_length_control(value):
        """控制显示的长度"""
        return value[0:650]+"..." if len(value)> 650 else value
    
    @app.template_filter()
    def time_to_format(value):
        """日期格式"""
        from utils.choices import MONTHDICT
        year, month, day = value.year, value.month, value.day
        month_str = MONTHDICT.get(month)
        return "".join([month_str, " ", str(day), ", ",str(year)])

    @app.template_filter()
    def ym_to_china(value):
        year, month = value.split("-")
        return year + u"年" + month + u"月"

    @app.template_filter()
    def to_timestamp(value):
        return value.strftime('%Y-%m-%d %H:%M:%S') if value else value

def configure_context_processors(app):

    @app.context_processor
    def globals_():
        """有待改进.."""
        from models.essay import Essay, Type
        
        essays = Essay.query.filter_by(display=True).all()
        dates = [obj.ctime.date() for obj in essays]
        date_dict = {}
        for date in dates:
            ym = date.strftime("%Y-%m")
            if date_dict.has_key(ym):
                count = date_dict.get(ym) + 1
                date_dict[ym] = count
            else:
                date_dict.setdefault(ym, 1)

        types = Type.query.order_by('rank desc').all()

        return dict(date_dict=date_dict, types=types)



