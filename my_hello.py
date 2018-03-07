from flask import Flask,render_template
from flask_script import Manager,Server
from flask_bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)

moment = Moment(app)

manager = Manager(app)
manager.add_command("runserver",Server(use_debugger=True))

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('my_index.html',current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('my_user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('my_404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('my_500.html'),500

if __name__ == '__main__':
    app.run(host='192.168.163.128')
