from flask import Flask, render_template, request, redirect, url_for, session
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simulated user database
users = {
    "user1@gmail.com": {"name": "User One"},
    "user2@gmail.com": {"name": "User Two"}
}

# Simulated token store
tokens = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        if email in users:
            token = str(uuid.uuid4())
            tokens[token] = email
            session['email'] = email
            return render_template('login_success.html', email=email, token=token)
        else:
            return 'Invalid Email'
    return render_template('login.html')

@app.route('/access')
def access():
    token = request.args.get('token')
    if token in tokens:
        email = tokens[token]
        name = users[email]['name']
        return render_template('access.html', name=name, email=email)
    return 'Access Denied: Invalid Token'

@app.route('/replay', methods=['GET', 'POST'])
def replay():
    if request.method == 'POST':
        token = request.form.get('token')
        return redirect(url_for('access', token=token))
    return render_template('replay.html')

if __name__ == '__main__':
    app.run(debug=True)
