from die import Die

# Create a D6
die = Die()
# we create  an instace of Die with the default six sides

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    # We roll the die 100 times and store each roll in th elist results
    result = die.roll()
    results.append(result)

print(results)
