#User Albums:

def make_album (artist, album, track=''):
    music = {"album":album, "artist":artist}


    if track:
        music['track'] = track
    return music

while True:


    print ("if like to qiut enter 'q'")
    i_artist = input("Enter your artist Name: ").lower()

    if i_artist == 'q':
        break

    i_album = input("Enter your album name: ").lower()

    if i_album == 'q':
        break

    i_track = input("Enter your tracks: ").lower()

    if i_track == 'q':
        break

    full = make_album(i_artist, i_album, i_track)
    print(full)
