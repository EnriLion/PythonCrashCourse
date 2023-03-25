##Slicing a list

players =  ['charles', 'martina', 'michael', 'florence', 'eli' ]
print(players[0:3])

print(players[1:4])

#Omit the first index in a slice and starts at the beginning of the list 

print(players[:4])

#Allows the putput returns the end of your list in your roster 

print(players[:-3])

#You can include  a third value  in the brackets indicatingva slice. If a third value is included, this tells Python how many items to skip betweenitems in the specified range 

##Looping through a slice


players =  ['charles', 'martina',  'florence', 'eli' ]

print("Here are the first players on my team:")
for player  in players[:3]:
    print(player.title())


