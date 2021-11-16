# app/home/__init__.py

from flask import Blueprint

groceries = Blueprint('groceries', __name__)

from . import views