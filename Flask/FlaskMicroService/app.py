from flask import Flask
from models import db

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="",
    SQLALCHEMY_DATABASE_URI='mysql'
))
db.init_app(app)