from flask import Flask
from spacy.en import English
parser = English()
app = Flask(__name__)
app.secret_key = 'dontguessme584829038572'
from app import views