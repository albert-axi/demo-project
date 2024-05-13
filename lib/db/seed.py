#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Playlist, Song, Artist

if __name__ == '__main__':
    engine = create_engine('sqlite:////Users/albert-work/Development/set14-fet8/phase-3/demo-project/lib/db/playlist.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(User).all()
    session.query(Playlist).delete()
    session.query(Song).delete()
    session.query(Artist).delete()

    fake = Faker()
    
    users = []
    for i in range(10):
        user = User(username=fake.unique.name())

        # add and commit individually to get IDs back
        session.add(user)
        session.commit()
        users.append(user)
        
        playlists = []
        for i in range(random.randint(1,5)):
          playlist = Playlist(title=fake.unique.name())
          playlist.user_id = user.id
          playlists.append(playlist)
          
        session.bulk_save_objects(playlists)
        session.commit()
        
    artists = []
    for i in range(10):
        artist = Artist(name=fake.unique.name())

        # add and commit individually to get IDs back
        session.add(artist)
        session.commit()
        artists.append(artist)
        
        songs = []
        for i in range(random.randint(1,5)):
          song = Song(title=fake.unique.name(), album=fake.unique.name())
          song.artist_id = artist.id
          songs.append(song)
          
        session.bulk_save_objects(songs)
        session.commit()
        
    
    # playlists = session.query(Playlist).all()
    # songs = session.query(Song).all()
    
        
    
    
    
