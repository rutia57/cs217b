# Assignment 2: Databases

## How to run my code

### Requirements
I used Python 3.9.6, so my code is set up to work with this version.
The required modules are listed in `requirements.txt`, and can be installed by running the command `pip install -r requirements.txt`.

### Flask web server
To start my Flask web server, `cd` into this directory (`cs217b/assignment2/`), and then run the following command: 
```bash
$ python3 app.py
```
Then, go to http://127.0.0.1:5000 in a browser to access the website and use the text area to input text, or the file upload button to upload a .txt file. Click the submit button to process the text and view the results. On the results web page, click
the button at the bottom to go the database/list view (showing how many times each entity has been found so far), and on 
that page click the button at the bottom of the page to back to the NER visualization view. You can also click the reset button
to reset the counts of all entities to 0, so that the table of entities will be empty until you submit another text input.

### Docker image and container
To create a Docker image of this Flask webserver, use the `Dockerfile`. To do this, make sure Docker is installed, and then `cd` into this directory (`cs217b/assignment2/`) and run the following command:
```bash
$ docker build --tag ner .   
```
Then, to run the Docker container using this image, run the following command: 
```bash
$ docker run -dp 5000:5000 ner
```
You can then access the Flask server at http://127.0.0.1:5000.
Note: if you're running the server from Docker and are using the "upload" button to upload a .txt file, this .txt file has to be in the Docker container.
