import hashlib, random

def hash_password(password):
  hash_obj = hashlib.sha256(password.encode('utf-8'))
  return hash_obj.hexdigest()

def keygen():
  random.seed(None)
  return hash_password(str(random.randbytes))

