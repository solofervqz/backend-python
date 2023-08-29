from app import create_app # pylint: disable=import-self
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#app = create_app()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_UIR'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
