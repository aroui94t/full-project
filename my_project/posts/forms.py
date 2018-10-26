# forms.py members 
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField

class add_post(FlaskForm):
    title       = StringField('Title:')
    content     = TextAreaField('Content:s')
    Submit      = SubmitField('Create')

class del_post(FlaskForm):
    button = SubmitField('Remove') 
