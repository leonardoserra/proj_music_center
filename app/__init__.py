from flask import Flask, redirect, render_template, abort, request

def start_app():
  app = Flask(__name__)

  @app.route('/')
  @app.route('/home')
  def home():
    return render_template('index.html', page_title='HOMEPAGE')

  @app.route('/login', methods=['GET','POST'])
  def login():
    if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']
      if password == '0000' and username == 'daruma':
        return f'''<h1>LOGIN EFFETTUATO!</h1>
                    <p>username: {username}</p>
                    <a href="/home">TORNA ALLA HOME</a>
                '''

    return render_template('login.html',  page_title='LOGIN')

  @app.route('/strumenti')
  def strumenti():
    return render_template('strumenti.html', page_title='STRUMENTI')
  
  @app.route('/concerti')
  def concerti():
    return render_template('concerti.html', page_title='CONCERTI')

  @app.route('/strumenti/chitarre')
  def chitarre():
    return render_template('chitarre.html', page_title='CHITARRE')
  @app.route('/strumenti/batterie')
  def batterie():
    return render_template('batterie.html', page_title='BATTERIE')
  @app.route('/strumenti/bassi')
  def bassi():
    return render_template('bassi.html', page_title='BASSI')

  ##############################
  return app
  ##############################