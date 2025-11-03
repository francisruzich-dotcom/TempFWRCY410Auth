
from flask import Flask, request, jsonify, render_template
from app import create_user, login

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/api/create_user', methods=['POST'])
def api_create_user():
    data = request.get_json()
    username = data.get('username')
    name = data.get('name')
    password = data.get('password')
    if create_user(username, name, password, 'users'):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'User already exists'})

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if login(username, password, 'users'):
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run(debug=True)
