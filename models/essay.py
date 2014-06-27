# -*- coding: utf-8 -*-

import datetime

from flaskext.sqlalchemy import BaseQuery
# from flask.ext.sqlalchemy import BaseQuery

from extensions import db

class Type(db.Model):
    """文章分类"""
    __tablename__ = "essay_type"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    interfacename = db.Column(db.String(10))

    @property
    def essay_nums(self):
        return Essay.query.filter_by(type_id=self.id, display=True).count() or 0


class Essay(db.Model):
    '''文章
        type_id: 文章的类型
        title: 标题
        content: 内容
        ctime: 发布时间
        poster: 发布人
        is_reprinted: 是否转载
        reprinted_url: 转载的url地址
    '''
    
    __tablename__ = 'essay_essay'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('essay_type.id'))
    title = db.Column(db.String(50), default='')
    content = db.Column(db.String(100000), default='')
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)
    poster = db.Column(db.String(20), default="funcle")
    is_reprinted = db.Column(db.Boolean, default=False)
    reprinted_url = db.Column(db.String(200), default='')
    display = db.Column(db.Boolean, default=False)

    @property
    def ptype(self):
        return Type.query.get(self.type_id)

    @property
    def comment_num(self):
        return Comment.query.filter_by(essay_id=self.id).count()
        
class Comment(db.Model):
    '''文章评论'''

    __tablename__ = 'essay_comment'
    
    id = db.Column(db.Integer, autoincrement=True, 
        primary_key=True)
    essay_id = db.Column(db.Integer, db.ForeignKey('essay_essay.id'))
    username = db.Column(db.String(20))
    comment = db.Column(db.String(500))
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)
    req_ip = db.Column(db.String(20), default="")
    up_num = db.Column(db.Integer, default=0)
    low_num = db.Column(db.Integer, default=0)

