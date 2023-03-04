import sys
sys.path.append('../')

from flask import Flask, render_template, request
from process_text import SpacyDocument

app = Flask(__name__)

@app.get("/")
def home_page():
    return render_template('input_page.html')

@app.post("/processed_text")
def input_text():
    text = request.form['input_text']
    doc = SpacyDocument(text)
    with open('static/css/main.css') as f:
        styling = f.read()
    return f"<style>{styling}</style>" + \
        doc.get_entities_with_markup()

if __name__ == '__main__':
    app.run(debug=True)
