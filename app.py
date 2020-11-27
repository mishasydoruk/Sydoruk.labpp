from flask import Flask
from gevent.pywsgi import WSGIServer

from Models import User
from Models import Song
from Models import Playlist

from sqlalchemy import Column, Integer, String, ARRAY, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)

engine = create_engine('postgresql://ppadmin:admin@localhost/ppdb', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
#session.commit()


#for instance in session.query(User).order_by(User.id):
#    print(instance)



@app.route('/api/v1/hello-word-2')
def index():
    return "Hello world 2"

if __name__=="__main__":
    WSGIServer(('', 5000), app).serve_forever()


