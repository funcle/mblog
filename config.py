# -*- coding: utf-8 -*-

import sae.const 

DEBUG = False
TESTING = False
SQLALCHEMY_ECHO = False

SECRET_KEY = 'gb\xe2\x14\xbc\xdcA\x82\x82A\x93$\x14T\x93\xb0\xcd\x94)x`\xad\xcbQ'

#mysql://username:password@server:port/db 
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB) 
# SQLALCHEMY_DATABASE_URI = 'postgresql://jiangnan:123456@127.0.0.1:5432/t3ngame'

UPLOAD_ESSAY_FOLDER = "static/images/essay_floder/"
UPLOAD_PHOTO_FOLDER = "static/images/photo_floder/"