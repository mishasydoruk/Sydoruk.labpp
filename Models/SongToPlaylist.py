from sqlalchemy import Column, Integer, String, ARRAY, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base



with open("./config.cfg",'r',encoding="utf-8") as config:
    connection_string = config.readline()
engine = create_engine(connection_string, echo=True)
Base = declarative_base()

class SongToPlaylist(Base):
    __tablename__ = 'playlists'
    song_id = Column(Integer)
    plyalist_id = Column(Integer)

    def __init__(self, song_id, playlist_id):
        self.song_id = song_id
        self.playlist_id = playlist_id



Base.metadata.create_all(engine)