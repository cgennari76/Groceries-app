#from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime

class Grocery(db.Model):
    __tablename__ = 'grocery'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Grocery: {}>'.format(self.name)