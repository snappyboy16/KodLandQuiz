from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello'


@app.route('/register')
def register():
    return 'Register'


@app.route('/login')
def login():
    return 'Login'


@app.route('/quiz')
def quiz():
    return 'Quiz'


@app.route('/leaders')
def leaders():
    return 'Leaders'


if __name__ == '__main__':
    app.run(debug=True)
