from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

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
    if request.method == 'POST':
        try:
            event_details = {
                'name': request.form['name'],
                'date': datetime.strptime(request.form['date'], '%Y-%m-%d'),
                'location': request.form['location']
            }
            events.append(event_details)
            flash('Event created successfully!', 'success')
        except ValueError as e:
            flash(f'Error creating event: {str(e)}', 'error')
        return redirect(url_for('home'))
    return render_template('create_event.html')

@app.route('/register/<int:event_id>', methods=['GET', 'POST'])
def register(event_id):
    if request.method == 'POST':
        registration_details = {
            'event_id': event_id,
            'name': request.form['name'],
            'email': request.form['email']
        }
        registrations.append(registration_details)
        flash('Successfully registered!', 'success')
        return redirect(url_for('home'))
    if event_id < len(events):
        event = events[event_id]
    else:
        flash('Event does not exist.', 'error')
        return redirect(url_for('home'))
    return render_template('registration.html', event=event, event_id=event_id)

if __name__ == '__main__':
    app.run(debug=True)
