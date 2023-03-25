name = "ada lovelace"
print(name.title())

#the method .title() changes each word to title case, where each wprd begins with a capital letter 

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# the lower() is usually to store data 

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# this f{}{} types of strings are called f-strings the f is for format because python replaces as the name with its value


print(f"Hello, {full_name.title()}!")


full_name = "{} {}".format(first_name, last_name)

#F-strings were introduced in python 3.6 if you are using 3.5 to use the format()

print(full_name)

#Adding whitespace to strings with tabs or newlines

print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping Whitespace

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

favorite_language = favorite_language.rstrip()

print(favorite_language)

#More strip whitespace

favorite_language = ' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

