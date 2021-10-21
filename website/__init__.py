from flask import Flask
from flask_bootstrap import Bootstrap
from .views import views

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.register_blueprint(views)

    return app