import os
from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
@application.route('/index')
def index():
    return render_template("index.html")


@application.route('/about')
def about():
    return render_template("about.html")


@application.route('/projects')
def projects():
    return render_template("projects.html")

    

if __name__ == '__main__':
    application.debug = True
    application.run()