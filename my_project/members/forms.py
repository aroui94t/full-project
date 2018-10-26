# forms.py members 
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField

class add_members(FlaskForm):
    username = StringField('Username:')
    email    = StringField('Email:')
    age      = IntegerField('Age:')
    password = PasswordField('Password:')
    Submit   = SubmitField('Regiter')