from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config
from .models import db
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)
          
        db.create_all()

    return app
