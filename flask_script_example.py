"""
flask_script_example
"""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    """
    index
    """
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    """
    user
    """
    return f'<h1>Hello, {name}</h1>'

if __name__== '__main__':
    manager.run()
