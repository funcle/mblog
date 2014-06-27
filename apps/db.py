# -*- coding: utf-8 -*-

import os
import time
import datetime
from flask import Blueprint, render_template, jsonify, request, current_app
from flask import url_for

from extensions import db
from models.essay import Type, Essay

admin_router = Blueprint('admin', __name__)

@admin_router.route('')
def index():
    ''''''
    return "@admin"

@admin_router.route('/essay/add', methods=["POST", "GET"])
def essay_add():
    
    types = Type.query.order_by('rank desc').all()
    msg = ''
    if request.method == "POST":

        types = request.form.get('types', '0')
        poster = request.form.get('poster', 'funcle')
        title = request.form.get('title', '')
        is_reprinted = request.form.get('is_reprinted', False)
        reprinted_url = request.form.get('reprinted_url', '')
        content = request.form.get('content', '')

        flag = True
        if int(types) == 0 or title == "":
            flag = False
        if is_reprinted and reprinted_url == "":
            flag = False
        
        essay = Essay.query.filter_by(title=title, content=content).all()

        if not flag:
            msg = u':）出错了，请填写完整所需信息。'
        elif essay:
            msg = u"请勿重复提交。";
        else:
            essay = Essay(type_id=types, title=title, content=content, poster=poster, is_reprinted=is_reprinted, reprinted_url=reprinted_url)
            db.session.add(essay)
            db.session.commit()
            msg = u'提交成功，作者审核后将会在前台显示。'
        # return msg
    return render_template('/admin/essay_add.html', 
        types=types,
        msg=msg)


def allowed_file(filename):
    """允许上传的文件类型"""
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif', 'jpeg'])
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@admin_router.route('/essay/pic_upload', methods=['POST'])
def essay_pic_upload():
    """图片上传"""
    from werkzeug import secure_filename

    if request.method == 'POST':
        f = request.files.get('file', None)
        if f and allowed_file(f.filename):

            current_date = datetime.date.today().strftime('%Y%m')
            project_path = current_app.config['UPLOAD_ESSAY_FOLDER']
            save_path = os.path.join(project_path, current_date)
            if not os.path.exists(save_path):
                os.makedirs(save_path)

            filename = secure_filename(f.filename)
            filename = '.'.join((''.join(str(time.time()).split('.')),\
                str(filename).split('.')[-1]))
            save_path_name = os.path.join(save_path, filename)
            f.save(save_path_name)
            url = "http://" + request.host + url_for('essay.index') + save_path_name
            
            return jsonify(imgUrl=url)
    return jsonify(error='上传错误.')