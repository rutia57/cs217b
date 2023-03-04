import sys
sys.path.append('../')

from process_text import SpacyDocument
import streamlit as st
import streamlit.components.v1 as components

file = 'input.txt'
text = "This is some example text with Yangyang and Ruth " + \
       "and Mr. Spongebob Squarepants and a 4th person " + \
       "in Boston on April 25th."

def initialize_session_vars(vars):
    for key, val in vars.items():
        if key not in st.session_state:
            st.session_state[key] = val

initialize_session_vars({
    'text' : text,
    'displayed_text' : '',
    'updated' : False
})

def update_displayed_text():
    text = st.session_state['text']
    doc = SpacyDocument(text)
    st.session_state['displayed_text'] = doc.get_entities_with_markup()

def update_text_from_file():
    if st.session_state['uploaded_file']:
        st.session_state['uploaded_text'] = st.session_state['uploaded_file'].getvalue().decode()
    st.session_state['text'] = st.session_state['uploaded_text']

def update_text_from_input():
    st.session_state['text'] = st.session_state['input_text']

st.header('Named Entity Recognition')
st.text_area('Input some text:', 
              value=text, 
              on_change=update_text_from_input, 
              key='input_text')
st.file_uploader('Or upload a file:', 
                 type=['.txt'], 
                 on_change=update_text_from_file, 
                 key='uploaded_file')
st.button('get entities', on_click=update_displayed_text)

css_file_path = "./streamlit-app/static/main.css"
with open(css_file_path) as f:
    styling = f.read()

if st.session_state['displayed_text'].strip() != '':
    components.html(f'<style>{styling}</style>' + \
                    f'<div class="box"><p class="text">{st.session_state["displayed_text"]}</p></div>',
                height=400)