import os
from flask import Flask, render_template
from swiper.models import Recipe
from . import db_conn
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    configure_app(app, test_config)
    db_conn.init_app(app)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        recipes = Recipe.query.all()
        return render_template("index.html", recipes=recipes)

    @app.route("/recipe")
    def recipe():
        recipes = Recipe.query.all()
        return render_template("recipe.html", recipes=recipes)

    return app

def configure_app(app, test_config):
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{os.path.join(app.instance_path, 'database.sqlite')}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass