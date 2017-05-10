# -*- coding:utf-8 -*-
"""
文件结构组织和说明可以参照文档 http://pm.oa.com/projects/telking/wiki/FLASK%E7%BD%91%E7%AB%99%E5%9F%BA%E6%9C%AC%E7%BB%93%E6%9E%84
初始化网站, http://docs.jinkan.org/docs/flask/patterns/appfactories.html
批量引入可以使用 from werkzeug.utils import import_string
"""
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_backstage import Admin


db = MongoEngine()

admin = Admin()


def register_blueprints(app):
    """
    加载蓝图 apps.register_blueprint(user, url_prefix='/user')    # 注册user蓝图，并指定前缀。
    """
    from apps.views.frontend import frontend

    app.register_blueprint(frontend)


def create_app(cfg):
    """  系统初始化   """

    # 初始化 Flask Application
    app = Flask(__name__)

    # 加载配置文件,默认使用 apps/config.cfg ( 项目中的apps/config.ini 是范例文件 )
    app.config.from_pyfile(cfg)

    # 注册蓝图
    register_blueprints(app)

    db.init_app(app)  #  注册数据库

    admin.init_app(app)  #  初始化flask_backstage

    # 注册所有的ModelView
    from apps.cadmin import create_cadmin
    create_cadmin(app)

    return app
