from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    date = db.Column(db.DateTime)

    def __repr__(self) -> str:
        return f"<User(id='{self.id}', username='{self.username}')>"

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
        }
