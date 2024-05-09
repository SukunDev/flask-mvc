import sys
from flask import render_template

from models.user import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    return render_template('index.html')