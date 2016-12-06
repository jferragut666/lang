from app import app, parser
from flask import render_template
import wtforms
import flask_wtf

@app.route('/')
def main():
    form = RequestForm()
    if form.validate_on_submit():
        parsedData = parser(form.sentence.data)
        print parsedData
    
    return render_template('base.html', form=form, title = "home")

class RequestForm(flask_wtf.FlaskForm):
    sentence = wtforms.StringField('sentence', [wtforms.validators.InputRequired()])
    submit = wtforms.SubmitField()
    
    