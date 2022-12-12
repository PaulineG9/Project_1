from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import  DataRequired, Email

class ContactForm(FlaskForm):
	name 	= StringField(label='Enter your name', validators=[DataRequired()])
	email 	= StringField(label='Enter your email', validators=[DataRequired(), Email(granular_message=True)])
	message = TextAreaField(label='Message')
	submit 	= SubmitField(label="Shoot")