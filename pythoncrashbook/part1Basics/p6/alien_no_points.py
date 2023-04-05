#Using get() to Access Values

alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) 

#this will get us a traceback due 

#the get() method to set a default value that will be returned if the requested key doesn't exist.

#the get() method requires a key as a first argument you can pass the value to be returned if the key doesn't exist:

point_value = alien_0.get('points', 'No point value assinged.')
print(point_value)

#if the key 'points' exists in the dictionary, you'll get the corresponding value. If it doesn't, you get the default value. In this case, points doesn't exist and we get a clean message instead of an error:

#If there's a chance the key you're asking for might not exist, consider using the get() method insted of the square bracket notation.

#Note: If you leave out the second argument in the call to get() and the key doesn't exist, Python will return the value None. The special value None means "no value exist" This is not an error: it's a special value meant to indicate the absence of a value You'll see more users for None in Chatper 8


