from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from db.models import User, Playlist, Artist, Song

engine = create_engine('sqlite:////Users/albert-work/Development/set14-fet8/phase-3/demo-project/lib/db/playlist.db')
Session = sessionmaker(bind=engine)
session = Session()

def clear():
  clrs = lambda: os.system('clear')
  clrs()

def main_menu():
  print("""
          1 - View Playlists
          2 - View Songs
          3 - View Artists
          4 - Add Song
          5 - Add Artist
          0 - Exit
        """)
  

def prompt_input():
  selected = int(input("Enter Your Choice: "))
  if selected > 5:
      return None
  else:
    return selected
    
def render(value):
  clear()
  if value == 1:
    clear()
    render_playlists()
  elif value == 2:
    clear()
    render_songs()
  elif value == 3:
    render_artists()
  elif value == 4:
    add_song()
  elif value == 5:
    add_artist()
  else:
    exit()
    
def add_song():
  title = input("Song Title: ")
  album = input("Song Album: ")
  
  new_song = Song(title, album)
  session.add(new_song)
  session.commit()
  
def add_artist():
  pass
      
def render_artists():
  artists = session.query(Artist).all()
  for a in artists:
    print(a)

def render_songs():
  songs = session.query(Song).all()
  for s in songs:
    print(s)

def render_playlists():
  print("render playlists")
  


def exit_app():
  pass
  

  
  