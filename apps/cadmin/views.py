# -*- coding:utf-8 -*-
"""
ModelView文件
"""
from flask_backstage import BaseModelView
from flask_backstage import admin_create_required

class PostView(BaseModelView):
	column_labels = dict(title="标题", content="内容", time="发布时间", image='图片')
	name = "文章"
	image_list = ['image']
	create_templates = 'frontend/create_post.html'
	edit_templates = 'frontend/edit_post.html'
	can_create = False
	can_delete = False
	can_edit = False

	def is_accessible(self):
		return admin_create_required(role=0)
