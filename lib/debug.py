#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import User, Playlist, Artist, Song

if __name__ == '__main__':
    
    engine = create_engine('sqlite:////Users/albert-work/Development/set14-fet8/phase-3/demo-project/lib/db/playlist.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
