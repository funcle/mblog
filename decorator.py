# -*- coding: utf-8 -*-

from functools import wraps

from extensions import db

def db_commit(f):
    @wraps(f)
    def decorated_func(*args, **kws):
        try:
            result = f(*args, **kws)
        except Exception, e:
            db.session.rollback()
            db.session.close()
            raise e
        finally:
            try:
                db.session.commit()
            except Exception, e:
                db.session.rollback()
                db.session.close()
                raise e
        return result
    return decorated_func