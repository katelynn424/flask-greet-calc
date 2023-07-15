from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_page():
    """returns welcome"""
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    """returns welcome home"""
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    """returns welcome back"""
    return "welcome back"