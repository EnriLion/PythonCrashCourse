def make_album(artist,album):
    """Definition to create a dictionary of an album"""
    disc = {'artist':artist, 'album':album}
    return disc
person = make_album('julian','the new abnormal')
print(person)
print("\n")
person = make_album('jonny','portamento')
print(person)
print("\n")
person = make_album('john','giant steps')
print(person)
print("\n")

def make_album(artist,album,song=None):
    """Definition to create a dictionary of an album"""
    disc = {'artist':artist, 'album':album}
    if song:
        disc['song'] = song 
    return disc
person = make_album('julian','the new abnormal',song=9)
print(person)
print("\n")
person = make_album('john','giant steps')
print(person)
print("\n")
