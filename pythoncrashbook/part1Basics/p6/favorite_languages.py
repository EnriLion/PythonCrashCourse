#A list in a dictionary

favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:# loop throguh each person list favorite languages
        print(f"\t{language.title()}")

#To refine this program even further we could include an if statement at the beginning of the dictionary's for loop to see whether each person ahs more than one favorite language by examining the value of len(languages(. I f a person has more than one favorite, the output would stay the same. If the person has only one favorite language, you could change the woding to reflect that. For example, you cold say Saran's favorite language is C

#Note: You should not nest lists and dictionaries too deeply, if youre nesting items much deeper than what you see in the preceding examples or your working with someone else code with significant levels of nesting, most likely a simpler way to solve the problem exists.


