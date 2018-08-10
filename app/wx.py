# -*- coding: utf-8 -*-
from flask import Flask
from werobot.contrib.flask import make_view
from robot import robot


app = Flask('Wx')
app.config.from_object('config')
config = app.config
app.add_url_rule(rule='/robot/',
                 endpoint='werobot',
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])