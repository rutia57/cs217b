# Assignment 1: Web Services

## How to run my code

### Requirements
I used Python 3.9.6, so my code is set up to work with this version.
The required modules are listed in `requirements.txt`, and can be installed by running the command `pip install -r requirements.txt`.

### RESTful API
To run my Flask RESTful API program, `cd` into this directory (`cs217b/assignment1/`) and run the following command: 
```bash
$ python flask-restful-api/NER.py
```
Running the following `curl` commands in the terminal (from the directory where `input.txt` is stored – here, it is in this same `cs217b/assignment1/` folder) should now output information about the service and the NER results, respectively:
```bash
$ curl http://127.0.0.1:5000/api
$ curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```

### Flask web server
To start my Flask web server, `cd` into this directory (`cs217b/assignment1/`) and if the RESTful API is still running, quit it by pressing CTRL+C (so that the port 5000 is not in use). Then, run the following command: 
```bash
$ python flask-webserver/NER.py
```
Then, go to http://127.0.0.1:5000 in a browser to access the website and use the text area to input text. Click the submit button to process the text and view the results.

### Streamlit application
To start my Streamlit application, `cd` into this directory (`cs217b/assignment1/`) and run the following command: 
```bash
$ streamlit run streamlit-app/NER.py
```
The application might take a few seconds to load, because the first time the code is run it needs to download the `nltk` tagger.<br>
Then, go to http://localhost:8501/ in a browser to access the application. To input text, either type it in the input text area or upload a .txt file by clicking the "browse files" button or dragging the file into the file upload area. To process the text and view the results, click the "Submit" button. The NER results will be displayed below in the Named Entities tab, the dependency tree for each sentence will be displayed in the Dependency Parse tab, and the text tagged for part of speech will be displayed in the Parts of Speech tab.
