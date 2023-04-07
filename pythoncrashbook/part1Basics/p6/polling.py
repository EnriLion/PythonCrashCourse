favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'python',
        'phil': 'ruby',
        }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#Looping through all-key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping through all the keys in a dictionary
print("\n")

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
for name in favorite_languages.keys():
    print(name.title())

#Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote
# for name in favorite_languages:
# for name in favorite_languages.keys():
# so its not necessary use wirthe the .keys() method

friends = ['phil', 'sarah'] #We print each person name
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:# we check if friends list have the same keys as names in that case printing 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

#Let's find out if Erin took the poll:
print("\n")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Looping through dictionary's keys in a particular order
print("\n")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping through all values in a dictionary
#Using the method values we could loop through the value elements
print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique:

print("\n")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):# we use set() to pull out the unique languages in favorite_languages values to print through the loops using the set to show the results without repetition.
    print(language.title())

#Note: You can build a set directly using braces and separating the elements with commas:
print("\n")
languages = {'python', 'ruby', 'python', 'c'}
print(languages)
#Notes: It's easy to mistake sets for dictionaries because they're both wrapped in braces. When you see braces but no key-value pairs, you're probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific-order

#Polling

Should_taken = ['edward', 'jen', 'richarldison', 'mierdin', 'jane']

for name in favorite_languages.keys():
    if name in Should_taken:
        print(f"Congratulations for taking the poll, {name.title()}")
    else:
        print(f"Please take the poll {name.title()}")

    

