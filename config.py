# -*- coding: utf-8 -*-

import sae.const 

DEBUG = False
TESTING = False
SQLALCHEMY_ECHO = False

SECRET_KEY = 'gb\xe2\x14\xbc\xdcA\x82\x82A\x93$\x14T\x93\xb0\xcd\x94)x`\xad\xcbQ'

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (sae.const.MYSQL_USER, sae.const.MYSQL_PASS, sae.const.MYSQL_HOST, sae.const.MYSQL_PORT, sae.const.MYSQL_DB) 

UPLOAD_ESSAY_FOLDER = "static/images/essay_floder/"
UPLOAD_PHOTO_FOLDER = "static/images/photo_floder/"