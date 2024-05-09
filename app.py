from flask import Flask
from flask_migrate import Migrate

from models.user import db
from routes.home_bp import home_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(home_bp, url_prefix='/')


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)