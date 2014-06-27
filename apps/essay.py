# -*- coding: utf-8 -*-

import re
import datetime

from sqlalchemy import cast, Date
from flask import render_template, Blueprint, request, jsonify

from models.essay import Essay, Type, Comment
from extensions import db

essay_router = Blueprint('essay', __name__)

@essay_router.route('/', methods=['GET'])
def index():
    """首页"""
    
    essays = Essay.query.filter_by(
        display=True
        ).order_by('ctime desc').limit(3)

    return render_template('/essay/index.html', 
        essays=essays)

@essay_router.route('/<interfacename>/', methods=['GET'])
def types(interfacename=None):
    """根据类别显示出文章列表"""

    tobj = Type.query.filter_by(interfacename=interfacename).first()
    if not tobj:
        return u'<h1>404</h1>'

    essays = Essay.query.filter_by(
        type_id=tobj.id, 
        display=True
        ).order_by('ctime desc').all() or []

    return render_template('/essay/types.html',
        essays=essays)


@essay_router.route('/time-<ym>/', methods=['GET'])
def display_ym(ym=None):
    """根据年月显示出该月的文章列表"""

    ym_reg = re.compile(r'^\d{4}-\d{2}$')
    if not ym_reg.match(ym):
        return u'404'

    year, month = ym.split('-')
    current_year = datetime.date.today().year
    if not 1970<=int(year)<=current_year or not 0<int(month)<13:
        return u"404"

    start = datetime.date(int(year), int(month), 1)
    end = datetime.date(int(year), int(month)+1, 1) - datetime.timedelta(days=1)

    essays = Essay.query.filter(
        cast(Essay.ctime, Date)>=start, 
        cast(Essay.ctime, Date)<=end
        ).filter_by(
        display=True
        ).order_by('ctime desc').all() or []

    return render_template('/essay/types.html',
        essays=essays)


@essay_router.route('/essay_<id>/', methods=['GET'])
def essay_show(id):
    """文章显示"""

    essay = Essay.query.filter_by(id=id, display=True).first()
    if not essay:
        return u'<h1>404</h1>'

    return render_template('/essay/essay.html', 
        essay=essay)


@essay_router.route('/comments_<id>/', methods=['GET'])
def essay_comments(id):
    """文章评论"""

    essay = Essay.query.get(id)
    if not essay:
        return u'<h1>404</h1>'

    comments = Comment.query.filter_by(
        essay_id=id
        ).order_by('ctime desc').all()

    return render_template('/essay/comments.html', 
        essay=essay,
        comments=comments)


@essay_router.route('/comments/add', methods=['POST'])
def essay_comments_add():
    """提交文章评论"""

    essay_id = request.form.get("essay_id", "")
    username = request.form.get("username", "")
    comments = request.form.get("comments", "")
    req_ip = request.remote_addr
    
    if essay_id in ("",):
        return jsonify(status=False, msg=u'404')

    comment = Comment(essay_id=essay_id, username=username, comment=comments,
        req_ip=req_ip, low_num=0, up_num=0, ctime=datetime.datetime.now())
    db.session.add(comment)
    db.session.commit()
    
    return jsonify(status=True, msg=u'200')


