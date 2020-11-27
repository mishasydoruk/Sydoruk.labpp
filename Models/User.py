from sqlalchemy import Column, Integer, String, ARRAY, create_engine
from sqlalchemy.ext.declarative import declarative_base

with open("./config.cfg",'r',encoding="utf-8") as config:
    connection_string = config.readline()
engine = create_engine(connection_string, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    playlists_id = Column(ARRAY(Integer))

    def __init__(self, username, first_name, last_name, email, playlists_id, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.playlists_id = playlists_id
        self.password = password


Base.metadata.create_all(engine)