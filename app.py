from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    auth = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Book %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'POST':
        content_name = request.form['name']
        content_auth = request.form['auth']
        content_year = request.form['year']
        data = Todo(name = content_name, auth = content_auth, year = content_year)

        try:
            db.session.add(data)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        books = Todo.query.order_by(Todo.year).all()
        return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)