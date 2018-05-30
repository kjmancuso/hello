import os

import flask_bootstrap

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
flask_bootstrap.Bootstrap(app)


@app.route('/')
def index():
    data = request.environ
    environ = os.environ

    return render_template('index.html', data=data, environ=environ)


@app.route('/hello')
def hello():
    data = request.environ
    ra = data['REMOTE_ADDR']
    hello = '''
Hello, is it me you're looking for?
I can see it in your eyes
I can see it in your smile

You are coming from %s.
''' % ra
    return hello, 200


if __name__ == '__main__':
    app.run()
