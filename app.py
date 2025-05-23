from flask import Flask, render_template, request, redirect, session, url_for
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

# Simulated database of users with Google IDs
users = {
    "student1@gmail.com": {"google_id": "google-uid-123", "name": "Student One"},
    "student2@gmail.com": {"google_id": "google-uid-456", "name": "Student Two"},
}

# Simulated token store (not secure – just for demo)
tokens = {}

@app.route('/')
def index():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if email in users:
            # Simulate OAuth token issuance
            token = str(uuid.uuid4())  # Generate a random token
            tokens[token] = users[email]['google_id']  # Store token with Google ID
            session['user'] = {
                "email": email,
                "name": users[email]['name'],
                "google_id": users[email]['google_id'],
                "token": token
            }
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Unauthorized email")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/admin/tokens')
def show_tokens():
    return f"<pre>{tokens}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
