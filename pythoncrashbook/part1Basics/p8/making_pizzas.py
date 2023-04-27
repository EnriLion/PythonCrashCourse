# import pizza

#pizza.make_pizza(16, 'pepperoni')
#pizza.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

#python call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot producing the same output as the original program.

#using the import followed by the name of the module makes every function from the module available in our program if we use this kind of import in an entire module named module_name.py each finction in the module is available through the following syntax:

#-module_name.function_name():

##Importing specific functions

#import a specific function from a module. here's the general syntax for this approach:

#-from module_name import function_name

#import as many functions as we want from a module by separating each function's name with a comma:

#-from module_name import function_0, function_1, function_2

#the makin_piza would look like this if we want to import just the function

#-from pizza import make_pizza

#-make_pizza(16, 'pepperoni')
#-pizza.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

#with that syntax we don't need to use the dot notation when you call a function. Because we've explictly imported the funcion make_pizza() in the import statement, we can call it by name when we use the function

##Using as to Give a function an alias

#We could import a function as an alias if we know that is to long
#for example give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as keyword renames a function usin the alias you provide:

# from pizza import make_pizza as mp

# mp(16, 'pepperoni')
# mp(12, 'mushrooms','green peppers', 'extra cheese')

#the general syntax for providing an alias:

#-from module_name import function_name as fn

##Using as to Give a module an alias

#we could also provide an alias for a module name:

# import pizza as p

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

# the general syntax for this approach is:

# - import module_name as mn

##Importing all functions in a module

#You can tell Python to import every function in a module by using the asterisk(*) operator:

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

#the asterisk in the import statement tells python to copy every fucntion from the module pizza into this program file(however its best not to use this approach when you're working with larger modules that you didn't write: if the module has a dunction name that matches an existing name in your project)
