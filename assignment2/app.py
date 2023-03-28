import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.sep.join(dir_path.split(os.path.sep)[:-1]))

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from process_text import SpacyDocument

app = Flask(__name__)

app.config['SECRET_KEY'] = '9d9527c141770801b9c02e1d43438071'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_entities.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Entity(db.Model):
    entity_text = db.Column(db.String(120), primary_key=True, unique=True, nullable=False)
    count = db.Column(db.Integer, unique=False)
    def __repr__(self):
        return f'Entity "{self.entity_text}" has appeared {self.count} times.'

def create_all():
    with app.app_context():
        db.create_all()

create_all()
    
@app.route("/", methods=['GET','POST'])
def home_page():
    if request and request.form and 'input_text' in request.form:
        text = request.form['input_text']
    else:
        text = 'This is some example text with Yangyang and Ruth and Mr. Spongebob Squarepants and a 4th person in Boston on April 25th.'
    return render_template('input_page.html', displayed_text = text)

@app.post("/markup_entities")
def view_results():
    text = request.form['input_text']
    if 'displayed' in request.form:
        displayed_text = request.form['displayed']
    else:
        text_file = request.form['input_file']
        if text_file:
            with open(text_file) as f:
                text = f.read()
        doc = SpacyDocument(text)
        for e in doc.get_entities():
            if e[3] in [x.entity_text for x in Entity.query.all()]:
                entity = Entity.query.filter_by(entity_text=e[3]).first()
                entity.count += 1
                db.session.commit()
            else: 
                entity  = Entity(entity_text = e[3], count = 1)
                db.session.add(entity)
                db.session.commit()
        displayed_text = doc.get_entities_with_markup()
    return render_template('markup_entities.html', displayed_text = displayed_text, input = text)

@app.post("/list_entities")
def view_list():
    if 'input_text' in request.form:
        input_text = request.form['input_text']
    else:
        input_text = ''
    if 'displayed' in request.form:
        displayed_text = request.form['displayed']
    else:
        displayed_text = ''
    if 'reset' in request.form:
        for e in Entity.query.all():
            db.session.delete(e)
            db.session.commit()
    query_result = Entity.query.order_by(Entity.count.desc()).all()
    return render_template('list_entities.html', query_result=query_result, displayed_text=displayed_text, input=input_text)

if __name__ == '__main__':
    app.run(debug=True)
