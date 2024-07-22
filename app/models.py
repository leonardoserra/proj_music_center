from . import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# con sqlite 'sqlite://database.db'
# con mysql 'mysql://username:password@host:port/database_name'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://music_centre.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CastoroInformatico1992!@localhost:3306/music_centre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model): #questo fa CREATE TABLE prodotto
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  password = db.Column(db.String(255), nullable=False)
  
class Instrument(db.Model): #questo fa CREATE TABLE prodotto
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  description = db.Column(db.Text)
  price = db.Column(db.Float(2), nullable=False)
  product_type = db.Column(db.String(255), nullable=False)

  def __repr__(self):
    return f'Strumento {self.name}'

class Concert(db.Model): #questo fa CREATE TABLE prodotto
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False) #string vuole il numero dei chars
  price = db.Column(db.Float(2))
  product_type = db.Column(db.String(255))

class Person(db.Model): #questo fa CREATE TABLE prodotto
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  surname = db.Column(db.String(255), nullable=False)
  product_type = db.Column(db.String(255))

class Group(db.Model): #questo fa CREATE TABLE prodotto
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  price = db.Column(db.Float)
  group_members = db.Column(db.String(255))