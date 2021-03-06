from sqlalchemy import Column, Integer, String, ARRAY, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base



with open("./config.cfg",'r',encoding="utf-8") as config:
    connection_string = config.readline()
engine = create_engine(connection_string, echo=True)
Base = declarative_base()

class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_public = Column(Boolean)

    def __init__(self, name, is_public):
        self.name = name
        self.is_public = is_public



Base.metadata.create_all(engine)