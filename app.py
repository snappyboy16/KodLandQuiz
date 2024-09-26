from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/leaders')
def leaders():
    return render_template('leaders.html')


if __name__ == '__main__':
    app.run(debug=True)
