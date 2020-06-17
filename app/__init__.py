from flask import Flask
from flask import Flask, render_template, redirect
from .config import Config
from .models import db
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)
CORS(app)

from .routes import workoutplan  # noqa
app.register_blueprint(workoutplan.bp)
# app.register_blueprint(deck.bp)
# app.register_blueprint(user.bp)
# app.register_blueprint(completed.bp)
# app.register_blueprint(favorites.bp)
# app.register_blueprint(deck.searchbp)
