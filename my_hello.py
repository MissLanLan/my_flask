from flask import Flask
from flask_script import Manager,Server

app = Flask(__name__)

manager = Manager(app)
manager.add_command("runserver",Server(use_debugger=True))


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
