from app import db
from . import groceries
from flask import render_template, request, redirect, Blueprint
#from ..models import Grocery
from app.models import Grocery

@groceries.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        new_stuff = Grocery(name=name)

        try:
            db.session.add(new_stuff)
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem adding new stuff."

    else:
        groceries = Grocery.query.order_by(Grocery.created_at).all()
        return render_template('index.html', groceries=groceries)