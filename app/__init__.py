from flask import Flask
from spacy.en import English

app = Flask(__name__)
app.secret_key = 'dontguessme584829038572'
print "Building parser!"
#The parser is an english analyzing tool that can pick out grammer from a sentence using spacy.
app.parser = English()

from app import views


#if __name__ == '__main__':
