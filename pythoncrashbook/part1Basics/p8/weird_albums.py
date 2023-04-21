def make_album(artist,album,song=None):
    """Definition to create a dictionary of an album whit a while"""
    disc = {'artist':artist, 'album':album}
    if song:
        disc['song'] = song 
    return disc

while True:
    print("\nPlease tell me your artist")
    print("(enter 'q' at any time to quit)")

    n_artist = input("Artist name: ")
    if n_artist == 'q':
        break
    n_album = input("Album name: ")
    if n_album == 'q':
        break
    print("\nYou want to give the number of songs")
    enter_song = input("(enter 'n' to quit ot 'y' to continue)")
    if enter_song == 'n' or enter_song == 'N':
        break
    elif enter_song == 'y' or enter_song == 'Y':
        n_song = int(input("Numbers of songs:"))
        enter_song = int(0)
        enter_song = n_song
    break
try:
    if enter_song == n_song:
        person = make_album(n_artist, n_album, enter_song)
        print(person)
except:
    person = make_album(n_artist, n_album)
    print(person)

