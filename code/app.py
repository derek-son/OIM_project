# Defines basic structure of Flask app and calls the main routes

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import LostAndFoundItem

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/lostandfound'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    items = LostAndFoundItem.query.all()
    return render_template('index.html', items=items)

@app.route('/', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        # Assuming you have a 'LostAndFoundItem' model
        lost_item = LostAndFoundItem(name=name, description=description, is_lost=True)

        db.session.add(lost_item)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('report_lost.html')

@app.route('/report_found', methods=['GET', 'POST'])
def report_found():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        found_item = LostAndFoundItem(name=name, description=description, is_lost=False)

        db.session.add(found_item)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('report_found.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

# http://127.0.0.1:5000
