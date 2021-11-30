#use in the interpreter
import sys
sys.path.append("~/python-projects/simpleapp/app/groceries")
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, create_app
db = SQLAlchemy
app = create_app()
app.app_context().push()
from app.models import Grocery
obj = Grocery(name='milk')
db.session.add(obj)
db.session.commit()
Grocery.query.all()