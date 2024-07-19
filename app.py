#music center app

from flask import Flask, redirect, abort, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
  return render_template('index.html', title='HomePage')