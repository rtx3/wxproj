# -*- coding: utf-8 -*-
import os
from werobot.contrib.flask import make_view
from wx import app, config, robot






# start the server
if __name__ == "__main__":
    app.run(host=config['HOST'], port=config['PORT'], threaded=True)