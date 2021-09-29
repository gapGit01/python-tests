#Album

def make_album (artist, album, track=''):
    music = {"album":album, "artist":artist}

    if track:
        music['track'] = track
    return music

full = make_album('snoop dog', 'next episod', 12)
df = make_album ('gappiya', 'la lal a la')
print(full, df)

