from ideahub.db import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable = False)
    email = db.Column(db.String(255), unique=True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Id %r>' % self.id