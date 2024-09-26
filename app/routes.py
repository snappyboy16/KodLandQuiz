from app import app
from flask import render_template, request
from flask_login import current_user, login_user
from flask_login import login_required


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/quiz')
@login_required
def quiz():
    return render_template('quiz.html')


@app.route('/leaders')
@login_required
def leaders():
    return render_template('leaders.html')
