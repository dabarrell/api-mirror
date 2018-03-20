from flask import Flask
from .errorhandlers import error_handlers
from .config import configure_app

app = Flask(__name__)

import service.routes
app.register_blueprint(error_handlers)

configure_app(app)
