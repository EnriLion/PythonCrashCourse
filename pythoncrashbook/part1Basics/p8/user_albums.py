def make_album(artist, album, song):
    """Definition to create a dictionary of an album whit a while"""
    disk = {'artist':artist, 'album':album, 'song':song}
    return disk
while True:
    print("\nPlease tell me your artist")
    print("(enter 'q' at any time to quit)")

    n_artist = input("Artist name: ")
    if n_artist == 'q':
        break
    n_album = input("Album name: ")
    if n_album == 'q':
        break
    n_song = input("Number of songs: ")
    if n_album == str('q'):
        break

person = make_album(n_artist, n_album ,n_song)
print(person)

