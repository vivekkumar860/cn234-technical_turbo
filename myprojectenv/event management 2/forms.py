from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField, DateField,EmailField



class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
    
class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    date = DateField('Event Date', validators=[DataRequired()], format='%Y-%m-%d')
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    event_type = SelectField('Type', choices=[('conference', 'Conference'), ('seminar', 'Seminar'), ('workshop', 'Workshop')])
    image = FileField('Event Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Create Event')
