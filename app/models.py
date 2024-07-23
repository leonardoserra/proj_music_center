from . import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# con sqlite 'sqlite://database.db'
# con mysql 'mysql+mysqlconnector://username:password@host:port/database_name'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_centre.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:CastoroInformatico1992@localhost:3306/music_centre'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model): #questo fa CREATE TABLE users
  __tablename__ = 'users'
  # id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), primary_key=True, nullable=False) #string vuole il numero dei chars
  password = db.Column(db.Text, nullable=False)
  def __repr__(self):
    return f'Username {self.username}'
  
class Instrument(db.Model): #questo fa CREATE TABLE instruments
  __tablename__ = 'instruments'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  description = db.Column(db.Text)
  price = db.Column(db.Float(2), nullable=False)
  product_type = db.Column(db.String(255), nullable=False)
  image_url = db.Column(db.String(255), nullable=True)

  def __repr__(self):
    return f'Strumento {self.name}'

class Concert(db.Model): #questo fa CREATE TABLE concerts
  __tablename__ = 'concerts'
  title = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text)
  date = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False) #data, con server_default imposto il default
  price = db.Column(db.Float(2))
  image_url = db.Column(db.String(255), nullable=True)


class GroupMember(db.Model): #questo fa CREATE TABLE group_members
  __tablename__ = 'group_members'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False) #string vuole il numero dei chars
  surname = db.Column(db.String(255), nullable=False)
  instrument = db.Column(db.String(255))

class Group(db.Model): #questo fa CREATE TABLE group
  __tablename__ = 'groups'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  group_members = db.Column(db.String(255))