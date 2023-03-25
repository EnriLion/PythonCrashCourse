##Tuples

#Defining a tuple

dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])


#If we try to change the dimensions in the wrong way

# dimensions[0] = 250

#the previous example will give us a traceback

##Tuples are technically defined by the presence of a comma if we want to define one with only one element

my_t = (3,)

#Looping through all values in a tuple

for dimension in dimensions:
    print(dimension)

#Writing over a tuple

print("\n", "Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\n", "Modified dimensions:")
for dimension in dimensions:
    print(dimension)
