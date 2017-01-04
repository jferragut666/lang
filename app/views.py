from app import app
from flask import render_template
import wtforms
import flask_wtf
from lxml import etree
s = """<table cellpadding="2" cellspacing="2" border="0">
  <tr bgcolor="#DFDFFF" align="none"> 
    <td align="none"> 
      <div align="left">Number</div>
    </td>
    <td> 
      <div align="left">Tag</div>
    </td>
    <td> 
      <div align="left">Description</div>
    </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 1. </td>
    <td>CC </td>
    <td>Coordinating conjunction </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 2. </td>
    <td>CD </td>
    <td>Cardinal number </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 3. </td>
    <td>DT </td>
    <td>Determiner </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 4. </td>
    <td>EX </td>
    <td>Existential <i>there<i> </i></i></td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 5. </td>
    <td>FW </td>
    <td>Foreign word </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 6. </td>
    <td>IN </td>
    <td>Preposition or subordinating conjunction </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 7. </td>
    <td>JJ </td>
    <td>Adjective </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 8. </td>
    <td>JJR </td>
    <td>Adjective, comparative </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 9. </td>
    <td>JJS </td>
    <td>Adjective, superlative </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 10. </td>
    <td>LS </td>
    <td>List item marker </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 11. </td>
    <td>MD </td>
    <td>Modal </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 12. </td>
    <td>NN </td>
    <td>Noun, singular or mass </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 13. </td>
    <td>NNS </td>
    <td>Noun, plural </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 14. </td>
    <td>NNP </td>
    <td>Proper noun, singular </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 15. </td>
    <td>NNPS </td>
    <td>Proper noun, plural </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 16. </td>
    <td>PDT </td>
    <td>Predeterminer </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 17. </td>
    <td>POS </td>
    <td>Possessive ending </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 18. </td>
    <td>PRP </td>
    <td>Personal pronoun </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 19. </td>
    <td>PRP$ </td>
    <td>Possessive pronoun </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 20. </td>
    <td>RB </td>
    <td>Adverb </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 21. </td>
    <td>RBR </td>
    <td>Adverb, comparative </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 22. </td>
    <td>RBS </td>
    <td>Adverb, superlative </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 23. </td>
    <td>RP </td>
    <td>Particle </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 24. </td>
    <td>SYM </td>
    <td>Symbol </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 25. </td>
    <td>TO </td>
    <td><i>to</i> </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 26. </td>
    <td>UH </td>
    <td>Interjection </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 27. </td>
    <td>VB </td>
    <td>Verb, base form </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 28. </td>
    <td>VBD </td>
    <td>Verb, past tense </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 29. </td>
    <td>VBG </td>
    <td>Verb, gerund or present participle </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 30. </td>
    <td>VBN </td>
    <td>Verb, past participle </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 31. </td>
    <td>VBP </td>
    <td>Verb, non-3rd person singular present </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 32. </td>
    <td>VBZ </td>
    <td>Verb, 3rd person singular present </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 33. </td>
    <td>WDT </td>
    <td>Wh-determiner </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 34. </td>
    <td>WP </td>
    <td>Wh-pronoun </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 35. </td>
    <td>WP$ </td>
    <td>Possessive wh-pronoun </td>
  </tr>
  <tr bgcolor="#FFFFCA"> 
    <td align="none"> 36. </td>
    <td>WRB </td>
    <td>Wh-adverb </td>
  </tr>
</table>
"""
table = etree.XML(s)
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print dict(zip(headers, values)), row, col.text


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
        for span in parsedData.sents:
            sent = [parsedData[i] for i in range(span.start, span.end)]
            break
    lists = []
    try:    
        for token in sent:
            listy=[token.orth_, token.pos_, token.dep_,token.head.orth_]
            lists.append(listy)
            print(listy)
            
        #print parsedData
        return render_template('base.html', form=form, title = "home", data = lists)
    except: 
        return render_template('base.html', form = form, title = "home")    
        
class RequestForm(flask_wtf.FlaskForm):
    sentence = wtforms.StringField('Sentence', [wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField()

#Andrew's stuff, trying to create more pages

@app.route('/About')
def something():
    return 'Hellow Orld!'
#recording stuff so that if I screw up you can check where I changed stuff
#added the em stuff in design.css
#added </td> on line 196
#changed 1px to 0.0625em in base.html line 5,17
''' added this to the css page
body {
    background-color: green;
    background-image: url("http://images.clipartpanda.com/book-20clipart-KTn8jp8Tq.jpeg");
    background-position: right top;
    
    
}
and <body> </body> to the base.html page
'''
#Note to self: w3 schools is a good source


