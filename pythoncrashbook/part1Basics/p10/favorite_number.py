import json

fav = input("What is your favorite number? " )

file = 'favorite.json'
with open(file, 'w') as f:
    json.dump(fav, f)
    
