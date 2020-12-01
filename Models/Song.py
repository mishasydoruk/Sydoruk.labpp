from sqlalchemy import Column, Integer, String, ARRAY, create_engine
from sqlalchemy.ext.declarative import declarative_base

with open("./config.cfg", 'r', encoding="utf-8") as config:
    connection_string = config.readline()
engine = create_engine(connection_string, echo=True)
Base = declarative_base()

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)

    def __init__(self, name, author):
        self.name = name
        self.author = author


Base.metadata.create_all(engine)