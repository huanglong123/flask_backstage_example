# -*- coding:utf-8 -*-
"""
需要自定义使用的命令统一放到 apps/ulits/custom_manage.py 文件中方便管理
"""

from apps import create_app
from flask_script import Manager
from flask_script.commands import Clean, ShowUrls

app = create_app('config.cfg')
manager = Manager(app)
manager.add_command('clean', Clean())
manager.add_command('urls', ShowUrls())

if __name__ == '__main__':
    manager.run()
