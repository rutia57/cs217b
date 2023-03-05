import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.sep.join(dir_path.split(os.path.sep)[:-1]))

from process_text import SpacyDocument
import streamlit as st
from nltk.tokenize import sent_tokenize

file = 'input.txt'
text = "This is some example text with Yangyang and Ruth and Mr. Spongebob Squarepants and a 4th person in Boston on April 25th."

def initialize_session_vars(vars):
    for key, val in vars.items():
        if key not in st.session_state:
            st.session_state[key] = val


initialize_session_vars({
    'text' : text,
    'displayed_text' : '',
    'updated' : False,
    'dependency_trees' : None,
    'pos': None
})

def update_displayed():
    text = st.session_state['text']
    spacy_doc = SpacyDocument(text)
    st.session_state['displayed_text'] = spacy_doc.get_entities_with_markup()
    dep_svgs = []
    for sent in sent_tokenize(text):
        doc = SpacyDocument(sent)
        svg_img = doc.get_dep_img()
        dep_svgs.append(svg_img)
    st.session_state['dependency_trees'] = dep_svgs
    st.session_state['pos'] = spacy_doc.get_pos_tree()

def update_text_from_file():
    if st.session_state['uploaded_file']:
        st.session_state['uploaded_text'] = st.session_state['uploaded_file'].getvalue().decode()
    st.session_state['text'] = st.session_state['uploaded_text']

def update_text_from_input():
    st.session_state['text'] = st.session_state['input_text']


st.header('Named Entity Recognition')

col1, col2 = st.columns([8, 6])

with col1:
    st.text_area('Input some text:', 
                value=text, 
                on_change=update_text_from_input, 
                key='input_text',
                height=120)

with col2: 
    st.file_uploader('Or upload a file:', 
                    type=['.txt'], 
                    on_change=update_text_from_file, 
                    key='uploaded_file',
                    )

col3, col4, col5 = st.columns([11, 3, 3])

with col3:
    st.button('Submit', on_click=update_displayed)
with col4:
    st.button('snow ❄️', on_click=st.snow)
with col5:
    st.button('fun 🎈', on_click=st.balloons)

tab1, tab2, tab3 = st.tabs(['Named entities', 'Dependency parse', 'Parts of speech'])

css_file_path = "./streamlit-app/static/main.css"
with open(css_file_path) as f:
    styling = f.read()

with tab1:
    if st.session_state['displayed_text'].strip() != '':
        st.markdown(f'<style>{styling}</style>' + \
                    f'<div class="box"><p class="text">{st.session_state["displayed_text"]}</p></div>',
                    unsafe_allow_html=True)

with tab2:
    if st.session_state['dependency_trees']:
        for im in st.session_state['dependency_trees']:
            st.image(im, width=400, use_column_width='never')

with tab3:
    if st.session_state['pos']:
        st.markdown(f'<style>{styling}</style>' + \
                    f'<div class="box"><p class="text">{st.session_state["pos"]}</p></div>',
                    unsafe_allow_html=True)
