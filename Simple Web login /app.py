from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # This should be a more secure key in a real application
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# Dummy user credentials for demonstration purposes
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def signin():
    if "user" in session:
        return redirect(url_for('welcome', username=session['user']))
    return render_template('signin.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Validate credentials
    if username in users and users[username] == password:
        session['user'] = username
        return redirect(url_for('welcome', username=username))
    else:
        flash("Invalid credentials. Please try again.")
        return redirect(url_for('signin'))

@app.route('/welcome/<username>')
def welcome(username):
    if "user" in session and session['user'] == username:
        return render_template('welcome.html', username=username)
    else:
        flash("You need to login first.")
        return redirect(url_for('signin'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.")
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)
