#Returning a dictionary
def build_person(first_name, last_name):
     """Return a dictionary of information about a person"""
     person = {'first': first_name, 'last': last_name}
     return person #The previous dictionary is returned 

musician = build_person('jimi', 'hendrix')
print(musician)

#You could make more functions to accept optional values

print("\n")


def build_person(first_name, last_name, age=None):#The value none is a special value and we can used it as placeholder(Sometimes evaluates false)
     """Return a dictionary of information about a person"""
     person = {'first': first_name, 'last': last_name}
     if age:
         person['age'] = age #if thr function call includes a value for age that value is stored in the dicitionary 
     return person #The previous dictionarh is returned 

musician = build_person('jimi', 'hendrix', age=27)
print(musician)


