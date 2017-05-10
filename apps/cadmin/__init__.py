# -*- coding:utf-8 -*-
"""
初始化ModelView函数
"""
from apps.models.post import Post
from apps.cadmin.views import PostView
from flask_backstage import CAdmin

def create_cadmin(app=None):
    cadmin = CAdmin(app)
    cadmin.add_view(PostView(Post))