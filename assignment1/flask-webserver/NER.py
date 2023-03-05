import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.sep.join(dir_path.split(os.path.sep)[:-1]))

from flask import Flask, render_template, request
from process_text import SpacyDocument

app = Flask(__name__)
    
@app.route("/", methods=['GET','POST'])
def home_page():
    if request and request.form and 'input' in request.form:
        text = request.form['input']
    else:
        text = 'This is some example text with Yangyang and Ruth and Mr. Spongebob Squarepants and a 4th person in Boston on April 25th.'
    return render_template('input_page.html', displayed_text = text)

@app.post("/processed_text")
def input_text():
    text = request.form['input_text']
    doc = SpacyDocument(text)
    return render_template('output_page.html', displayed_text = doc.get_entities_with_markup(), input = text)

if __name__ == '__main__':
    app.run(debug=True)
