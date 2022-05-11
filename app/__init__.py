from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv#
import os#

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()# load env file


def create_app(testing = None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #deal with database
    if testing is None:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")#use env file
    else:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI_TEST")#use env file

    from app.models.cats import Cat
    from app.models.humans import Human

    db.init_app(app) #initials sqalchemy object the database
    migrate.init_app(app, db)

    from .routes.cats import cats_bp
    app.register_blueprint(cats_bp)
    from .routes.humans import humans_bp
    app.register_blueprint(humans_bp)

    

    return app