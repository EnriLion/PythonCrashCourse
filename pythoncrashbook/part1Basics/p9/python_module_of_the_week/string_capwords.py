#Functions
##string - Text Constants and Templates

#Python modules: https://pymotw.com/3/index.html

#The string module dates from the earluer version of Python and have been moved to the methods str objects. The string module retains several useful constants and  classes for working with str objects

#The function capwords capitalizes all of the words in a string.
import string

s = 'The quick brown fox jumped over the lazy dog.'

print(s)
print(string.capwords(s))
