# -*- coding: utf-8 -*-
from werobot import WeRoBot


robot = WeRoBot(token="token from init")
robot.config.from_pyfile("config.py")




@robot.filter("帮助")
def show_help(message):
    return """
        帮助
           """


@robot.text
def hello_world(message):
    return 'Hello World!'
    robot.run()
