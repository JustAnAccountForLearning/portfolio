import os
from flask import Flask, render_template

# Configure application
application = Flask(__name__, static_url_path="/static")
application.secret_key = 'tRAuBw7POnhTaOF7KwndlyAJj3BL90xK' # Randomly generated key

# Ensure templates are auto-reloaded
application.config["TEMPLATES_AUTO_RELOAD"] = True


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