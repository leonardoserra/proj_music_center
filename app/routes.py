from . import app
import os, random, hashlib
from flask import redirect, render_template, abort, request, url_for, session
from .models import db, User, Instrument, Concert, GroupMember, Group
from werkzeug.utils import secure_filename


# ----------------------- utils ---------------------------------
def hash_password(password):
  hash_obj = hashlib.sha256(password.encode('utf-8'))
  return hash_obj.hexdigest()

def keygen():
  random.seed(None)
  return hash_password(str(random.randbytes))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

# ------------------- login - logout ----------------------------

@app.route('/login', methods=['GET','POST'])
def login():
  message = ''
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=hash_password(password)).first()
    if user:
      session["username"] = username
      return redirect(url_for('index'))
    message = 'Credenziali non valide'

  return render_template('login.html',  page_title='LOGIN', message=message)

@app.route('/logout')
def logout():
  session.pop('username', None)    
  return redirect(url_for('index'))

# ------------------- index ----------------------------

@app.route('/')
@app.route('/home')
def index():
  instruments = Instrument.query.all()
  concerts = Concert.query.all()
  return render_template('index.html', page_title='HOMEPAGE', instruments=instruments,concerts=concerts)


# ------------------- strumenti ----------------------------

@app.route('/strumenti')
def strumenti():
  instruments = Instrument.query.all()
  return render_template('strumenti.html', page_title='STRUMENTI', instruments=instruments)



@app.route('/create-instrument', methods=['GET', 'POST'])
def create_instrument():
  if "username" in session and session["username"] == 'admin':
    if request.method == 'POST':
      name = request.form["name"]
      description = request.form["description"]
      price = float(request.form["price"])
      product_type =  request.form["product_type"]
      image_url =  'default.jpg'
      
      if 'image' in request.files:
        file = request.files['image']
        
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          image_url =(f'instrument-{product_type}-{name.replace(' ','_')}' + '.' + filename.rsplit('.', 1)[1]).lower()
          file.save(os.path.join('./app' + app.config['UPLOAD_FOLDER'], image_url))
        
      instrument = Instrument(name=name, description=description, price=price, product_type=product_type, image_url=image_url) # type:ignore
      db.session.add(instrument)
      db.session.commit()
      return redirect(url_for('strumenti'))
    return render_template('create_instrument.html')
  return redirect(url_for('index'))

@app.route('/update-instrument/<int:id>', methods=['GET', 'POST'])
def update_instrument(id):
  if "username" in session and session["username"] == 'admin':
    instrument = Instrument.query.get_or_404(id)
    if request.method == 'POST':
      name = request.form["name"]
      description = request.form["description"]
      price = float(request.form["price"])
      product_type =  request.form["product_type"]
      image_url =  instrument["image_url"]
      
      if 'image' in request.files:
        file = request.files['image']
        
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          old_path = './app/static/images/' + instrument["image_url"]
          if os.path.exists(old_path):
            os.remove(old_path)
          image_url =(f'instrument-{product_type}-{name.replace(' ','_')}' + '.' + filename.rsplit('.', 1)[1]).lower()
          file.save(os.path.join('./app' + app.config['UPLOAD_FOLDER'], image_url))
        
      instrument = Instrument(name=name, description=description, price=price, product_type=product_type, image_url=image_url) # type:ignore
      db.session.add(instrument)
      db.session.commit()
      return redirect(url_for('strumenti'))
    return render_template('update_instrument.html', item=instrument)
  return redirect(url_for('index'))

@app.route('/delete-instrument/<int:id>', methods=['POST'])
def delete_instrument(id):
  if "username" in session and session["username"] == 'admin':
    if request.method == 'POST':
      instrument = Instrument.query.get_or_404(id)
      filepath = './app/static/images/' + instrument.image_url
      if os.path.exists(filepath):
        os.remove(filepath)
    db.session.delete(instrument)
    db.session.commit()
    return redirect(url_for('strumenti'))
  abort(401)
  

@app.route('/strumenti/chitarre')
def chitarre():
  guitars = Instrument.query.filter_by(product_type='guitar')
  return render_template('chitarre.html', page_title='CHITARRE', guitars=guitars)

@app.route('/strumenti/batterie')
def batterie():
  drums = Instrument.query.filter_by(product_type='drums')
  return render_template('batterie.html', page_title='BATTERIE', drums=drums)

@app.route('/strumenti/bassi')
def bassi():
  basses = Instrument.query.filter_by(product_type='bass')
  return render_template('bassi.html', page_title='BASSI',basses=basses)

#                 show strumenti

@app.route('/strumenti/chitarre/<int:id>')
def chitarra(id):
  item = Instrument.query.get_or_404(id)
  return render_template('show.html', page_title=f'Chitarra id {id}', item=item)

@app.route('/strumenti/batterie/<int:id>')
def batteria(id):
  item = Instrument.query.get_or_404(id)
  return render_template('show.html', page_title=f'Batteria', item=item)

@app.route('/strumenti/bassi/<int:id>')
def basso(id):
  item = Instrument.query.get_or_404(id)
  return render_template('show.html', page_title=f'Basso', item=item)

# ------------------- concerti ----------------------------

@app.route('/concerti')
def concerti():
  concerts = Concert.query.all()
  return render_template('concerti.html', page_title='CONCERTI', concerts=concerts)

@app.route('/create-concert', methods=['GET', 'POST'])
def create_concert():
  if "username" in session and session["username"] == 'admin':
    if request.method == 'POST':
      title = request.form["title"]
      description = request.form["description"]
      date = request.form["date"]
      price = float(request.form["price"])
      image_url = 'default.jpg'
      
      if 'image' in request.files:
        file = request.files['image']
        
        if file and allowed_file(file.filename):
          filename = secure_filename(file.filename)
          image_url =(f'concert-{date}-{title.replace(' ','_')}' + '.' + filename.rsplit('.', 1)[1]).lower()
          file.save(os.path.join('./app' + app.config['UPLOAD_FOLDER'], image_url))
        
      concert = Concert(title=title, description=description, price=price, date=date, image_url=image_url) # type:ignore
      db.session.add(concert)
      db.session.commit()
      return redirect(url_for('index'))
    return render_template('create_concert.html')
  return redirect(url_for('index'))

@app.route('/delete-concert/<int:id>', methods=['POST'])
def delete_concert(id):
  if "username" in session and session["username"] == 'admin':
    if request.method == 'POST':
      concert = Concert.query.get_or_404(id)
      path = './app/static/images/' + concert.image_url
      if os.path.exists(path):
        os.remove(path)
    db.session.delete(concert)
    db.session.commit()
    return redirect(url_for('concerti'))
  abort(401)

@app.route('/concerti/<int:id>')
def concerto(id):
  item = Concert.query.get_or_404(id)
  return render_template('show.html', page_title=f'Concerto', item=item)

# ------------------- admin ----------------------------
@app.route('/create-admin')
def create_admin():
  is_admin_created = User.query.filter_by(username='admin').first()
  if not is_admin_created:
    pwd = hash_password('admin')
    admin = User(username='admin', password=pwd) # type: ignore
    db.session.add(admin)
    db.session.commit()
  return redirect(url_for('index'))

# -------------------- error 404 ------------------------
@app.errorhandler(404)
def not_found_error(error):
  return render_template('404_error.html', error=error)

@app.errorhandler(401)
def not_authorized(error):
  return render_template('401_error.html', error=error)
