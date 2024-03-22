from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from forms import RegistrationForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management and flash messages

# Simulating a database with lists
events = []
registrations = []

@app.route('/')
def home():
    return render_template('index.html', events=events)

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    if form.validate_on_submit():
        # Assuming you save the filename or generate a path for the image
        filename = secure_filename(form.image.data.filename)
        form.image.data.save(os.path.join('path/to/save/images', filename))

        event_details = {
            'name': form.name.data,
            'organizer': form.organizer.data,
            'start_time': form.start_time.data.strftime('%Y-%m-%d %H:%M'),
            'end_time': form.end_time.data.strftime('%Y-%m-%d %H:%M'),
            'date': form.date.data.strftime('%Y-%m-%d'),
            'location': form.location.data,
            'capacity': form.capacity.data,
            'description': form.description.data,
            'event_type': form.event_type.data,
            'image': filename  # Store path or identifier for the image
        }
        events.append(event_details)  # Assuming events is a list. In a real app, you'd save this to a database.
        flash('Event created successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('create_event.html', form=form)


@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    form = RegistrationForm()
    if form.validate_on_submit():
        registration_details = {
            'event_id': event_id,
            'name': form.name.data,
            'email': form.email.data
        }
        registrations.append(registration_details)
        flash('Successfully registered!', 'success')
        return redirect(url_for('home'))
    if event_id < len(events):
        event = events[event_id]
    else:
        flash('Event does not exist.', 'error')
        return redirect(url_for('home'))
    return render_template('registration.html', event=event, event_id=event_id, form=form)

if __name__ == '__main__':
    app.run(debug=True)
