from ideahub.db import db

class IdeaTopic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable = False)
    description = db.Column(db.String(255), unique=True, nullable = False)
    posted_by = db.Column(db.String(255), nullable = False)
    

    def __repr__(self):
        return '<Id %r>' % self.id 