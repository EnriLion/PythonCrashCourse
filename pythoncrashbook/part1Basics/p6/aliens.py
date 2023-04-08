#Nesting

#Sometimes you will want to store multiple dictionaries in a list, or a list of itmes as a values in a citionary(nesting). Nesting is a powerful feature, as the following example:

#A list of dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens: #We loop through the list of dictionaries
    print(alien) #Printing each list

# A more realistic example we could use range() to create a fleet of 30 aliens:
# Make an empty list for storing aliens.
print("\n")

aliens = []

#Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#If we want to change the first three aliens to yellow, medium-speed and worth 10 points each, we could do this:
for alien in aliens[:3]:
    if alien['color'] == 'green': #if the aliens is change will changed the values of each keys: 
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10 
    elif alien['color'] == 'yellow':#we could use and elif statement and add more functionalities
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15 

#A list in dictionary




#Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created.
print(f"Total numbers of aliens: {len(aliens)}")

#range() returns a series of numbers, which just tells Python how many times we want the loop to repeat


