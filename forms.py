from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
import email_validator

class NameForm(FlaskForm):
    name = StringField('Имя пользователя: ', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')