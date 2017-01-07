from app import app
from flask import render_template
import wtforms
import flask_wtf
tableTerms = {'PRP$': 'Possessive pronoun ', 'VBG': 'Verb, gerund or present participle ', 'FW': 'Foreign word ', 'VBN': 'Verb, past participle ',
              'VBP': 'Verb, non-3rd person singular present ', 'WDT': 'Wh-determiner ', 'JJ': 'Adjective ', 'WP': 'Wh-pronoun ', 'VBZ': 'Verb, 3rd person singular present ',
              'DT': 'Determiner ', 'RP': 'Particle ', 'NN': 'Noun, singular or mass ', 'VBD': 'Verb, past tense ', 'POS': 'Possessive ending ', 'TO': 'to',
              'PRP': 'Personal pronoun ', 'RB': 'Adverb ', 'NNS': 'Noun, plural ', 'NNP': 'Proper noun, singular ', 'VB': 'Verb, base form ', 'WRB': 'Wh-adverb ',
              'CC': 'Coordinating conjunction ', 'LS': 'List item marker ', 'PDT': 'Predeterminer ', 'RBS': 'Adverb, superlative ', 'RBR': 'Adverb, comparative ',
              'CD': 'Cardinal number ', 'EX': 'Existential ', 'IN': 'Preposition or subordinating conjunction ', 'WP$': 'Possessive wh-pronoun ', 'MD': 'Modal ',
              'NNPS': 'Proper noun, plural ', 'JJS': 'Adjective, superlative ', 'JJR': 'Adjective, comparative ', 'SYM': 'Symbol ', 'UH': 'Interjection ', 'DET':'i am'}


#from run import parser
@app.template_filter()
def newLine(d):
  lst = [] 
  for i in d:
    lst.append(i+"\n")
  return lst
@app.route('/', methods=['post','get'])
def main():
    parsedData = 0
    
    form = RequestForm()
    if form.validate_on_submit():
        #parse sentence from the form
        parsedData = app.parser(form.sentence.data)
        sents = []
        sents = parsedData.sents
        print "parsed data sent!"
        for span in parsedData.sents:
            sent = [parsedData[i] for i in range(span.start, span.end)]
            print "data in sent!"
            break
        lists = []
        print "try success!"
        for token in sent:
            print token.tag_
            print tableTerms[token.tag_]
           
            listy=[token.orth_, token.tag_, token.dep_,token.head.orth_, tableTerms[token.tag_]]
            lists.append(listy)
            print(listy)
    else:        
        lists=[]
    return render_template('base.html', form=form, title = "home", data = lists)
    
        
class RequestForm(flask_wtf.FlaskForm):
    sentence = wtforms.StringField('Sentence', [wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField()

#Andrew's stuff, trying to create more pages

@app.route('/about-us')
def a():
    return render_template('Aboutus.html')

@app.route('/bootstrap')
def bootstrapstuff():
    form = RequestForm()
    return render_template('bootstrap.html', form = form, title = "yoyo")