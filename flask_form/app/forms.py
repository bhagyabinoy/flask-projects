# from flask_wtf import FlaskForm
# from wtforms.validators import Email, DataRequired
# from wtforms_components import EmailField

# class ContactForm(FlaskForm):
#     email = EmailField('Email Address', validators=[DataRequired(), Email()])

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Email, DataRequired
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
