from __future__ import absolute_import, unicode_literals
from flask import Flask, render_template
app = Flask('forum')

@app.route('/')
def hello_world():
    return render_template('index.html')
