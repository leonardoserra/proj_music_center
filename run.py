#music center app
"""
Questa è un app per gestire un negozio di musica
Avrà entita : 
- Prodotto(id, nome, prezzo, tipo:foreign key), 
- Concerto(nome, data, prezzo, gruppi:list[Gruppo])
- Gruppo(nome,membri:list[Persona])

db:
tabella prodotti
tabella gruppi

routes:
'home' o '/'
'/strumenti'
'/concerti'
'/concerti/<int:id>'
'/strumenti/chitarre'
'/strumenti/batterie'
'/strumenti/bassi'
'/strumenti/chitarre/<int:id>'
'/strumenti/batterie/<int:id>'
'/strumenti/bassi/<int:id>'
"""
from flask import Flask, redirect, abort, request, send_from_directory, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
  return render_template('index.html', title='HomePage')