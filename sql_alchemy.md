# SQL ALCHEMY

Serve a connettersi al db e a fare le query, è un ORM (Object Relational Mapping)

`pip install mysql-connector-python`
`pip install -U Flask-SQLAlchemy` : -U dice che fa l'auto update -> da eseguire nell ambiente corretto.



nel file models.py imposti la connessione al db

```py
from . import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

##connessione a db
# imposto la proprietà dell oggetto app con sqlite
## per mysql la connessione é cosi: 'mysql+mysqlconnector://username:password@host:port/database_name' con questo devi avere il db vuoto e poi popoli le tabelle
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```  
  
  
[Tipi Di Dato: DOCS](https://docs.sqlalchemy.org/en/20/core/type_basics.html#generic-camelcase-types)
  
Come definire le tabelle nel db coi models
```py
#creo entity che si riferisce a tabella 'persone' e gli definisco i data types sottoforma di class attributes


class Persona(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  age = db.Column(db.Integer)
```  

Una volta creati tutti i models per generare le tabelle e il database con quella struttura si usa flask shell e il comando è:  
```shell
flask shell
from app.models import db
db.create_all()
```
- Se la tabella è gia presente nel db non viene ricreata. Anche se è stato modificato il model. Quindi bisogna eliminare tutto il db.

Distruggere db:  
```shell
flask shell
from app.models import db
db.drop_all()
```
  
Per modificare il db senza droppare tutto esiste un pacchetto pip `Flask-Migrate` 


## CRUD
si usa `flask shell`

si usa 

```bash 
from app.models import db
mario = Persona(name='mario',age=23)
db.session.add(mario)
sara = Persona(name='sara',age=67)
db.session.add(sara)
db.session.commit() #salva la transaction ed esegue

```

Per fare `insert`
```bash
from app.models import db , Persona
db.create_all()
leo = Persona(name='Leonardo', age=32)
db.session.add(leo)
db.session.commit()
```


Per fare select dalle routes
```py
from .models import Persona
@app.route('/persone')
def persone():
  persone = Persona.query.all()
  return render_template('persone.html', persone=persone)
```
```jinja
<!-- ciclo persona -->
<h2>Elenco persone nel DB</h2>
  {% if persone %}
  <ul style="list-style:none;">
  {%for p in persone%}
    <li >Nome: {{p["name"]|safe}} Età: {{p["age"]|safe}}</li>
  {%endfor%}
  </ul>
  {% endif %}
```

altri modi di filtrare:
```py
#tutti i record
Persona.query.all() 
#tutti i record filtrati
Persona.query.filter_by(name='Mario Rossi').all()
#il primo che ha il filtro
Persona.query.filter_by(name='Mario Rossi').first()
#Il primo e quindi unico che ha id = 1
Persona.query.filter_by(id=1).first()
#filtro per primo id primary key
Persona.query.get(1)
#trova o errore 404
Persona.query.get_or_404(12)
```


