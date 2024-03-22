
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange
from flask_wtf.file import FileField, FileAllowed



class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
    
class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired()])
    organizer = StringField('Organizer', validators=[DataRequired()])
    start_time = DateTimeField('Start Time', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    end_time = DateTimeField('End Time', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    date = DateTimeField('Event Date', format='%Y-%m-%d', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired(), NumberRange(min=1)])
    description = TextAreaField('Description', validators=[DataRequired()])
    event_type = SelectField('Type', choices=[('conference', 'Conference'), ('seminar', 'Seminar'), ('workshop', 'Workshop'), ('social', 'Social')])
    image = FileField('Event Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Create Event')