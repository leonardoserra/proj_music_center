#app starts from here, with the servers todo
from app import start_app

app = start_app()
if __name__ == '__main__':
  app.run()