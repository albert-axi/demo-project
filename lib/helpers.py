def main_menu():
  print("""
          1 - View Artists
          2 - View Songs
          3 - View Playlists
          0 - Exit
        """)
  

def prompt_input():
  selected = int(input("Enter Your Choice: "))
  if selected > 3:
      return None
  else:
    return selected
    
def render(value):
  if value == 3:
    render_playlists()
  elif value == 2:
    render_songs()
  elif value == 1:
    render_artists()
  else:
    exit()
      
def render_artists():
  print("render artists")

def render_songs():
  print("render songs")

def render_playlists():
  print("render playlists")

def exit_app():
  pass
  

  
  