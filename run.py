"""
      file run: create app file
"""
import pymysql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app():
    """Initialize the core application."""

    app = Flask(__name__, instance_relative_config=False)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
        app.config.from_object("instance.config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
        app.config.from_object("instance.config.DevelopmentConfig")

    app.url_map.strict_slashes = False
    # Initialize Plugins
    db.init_app(app)

    with app.app_context():
        from routes import main_bp
        app.register_blueprint(main_bp)
        db.create_all()
    return app
