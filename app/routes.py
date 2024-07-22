from . import app
from flask import redirect, render_template, abort, request

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    if password == '0000' and username == 'daruma':
      return f'''<div style="margin:200px auto; text-align:center;">
                    <h1>LOGIN EFFETTUATO!</h1>
                    <p style="margin-bottom:35px">username: {username}</p>
                    <a style="text-decoration:none; color:#1a1a1a; padding: 10px; border: 1px solid black;" href="/home">TORNA ALLA HOME</a>
                </div>
              '''

  return render_template('login.html',  page_title='LOGIN')

@app.route('/')
@app.route('/home')
def home():
  return render_template('index.html', page_title='HOMEPAGE')


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

@app.route('/strumenti/chitarre/<int:id>')
def chitarra(id):
  item_name=f'chitarra numero: {id}'
  item_content=f'la descrizione della chitarra {id}'
  return render_template('show.html', page_title=f'Chitarra id {id}', item_name=item_name, item_content=item_content)

@app.route('/strumenti/batterie/<int:id>')
def batteria(id):
  item_name=f'batteria numero: {id}'
  item_content=f'la descrizione della batteria {id}'
  return render_template('show.html', page_title=f'Batteria', item_name=item_name, item_content=item_content)

@app.route('/strumenti/bassi/<int:id>')
def basso(id):
  item_name=f'basso numero: {id}'
  item_content=f'la descrizione del basso {id}'
  return render_template('show.html', page_title=f'Basso', item_name=item_name, item_content=item_content)

@app.route('/concerti/<int:id>')
def concerto(id):
  item_name=f'concerto numero: {id}'
  item_content=f'la descrizione del concerto {id}'
  return render_template('show.html', page_title=f'Concerto', item_name=item_name, item_content=item_content)
