# -*- coding:utf-8 -*-
"""

"""

from flask import Blueprint, render_template

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
	return render_template('frontend/index.html')