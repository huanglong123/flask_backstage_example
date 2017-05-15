# -*- coding:utf-8 -*-
"""
ModelView文件
"""
from flask_backstage import BaseModelView

class PostView(BaseModelView):
	column_labels = dict(title="标题", content="内容", time="发布时间")
	name = "文章"
