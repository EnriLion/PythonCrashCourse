from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
# die = Die()
# die_1 = Die()
# die_2 = Die()
# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)
# we create  an instace of Die with the default six sides

# Make some rolls, and store results in a list.
results = []
# for roll_num in range(100):
for roll_num in range(50_000):
    # We roll the die 100 times and store each roll in th elist results
    # We're not longer printing the results, we can increase the number of stimulated rolls to 1000
    # result = die.roll()
    result = die_1.roll() + die_2.roll()
    # After creating tow instances we roll dice
    results.append(result)

# print(results)
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# The max_resutl is the largest possible result(12) and the smallest(2)
# To analyze the rolls, we create the empty list frequencies
for value in range(1, max_result+1):
    # We analyze the results, we coulnt the number of results for each value
    # We loop through the possible values(1 thorugh 6)
    frequency = results.count(value)
    # how many times each number appears in results
    frequencies.append(frequency)
    # And then append this value to the frequencies list
# print(frequencies)

# Visualize the results.
# x_values = list(range(1, die.num_sides+1))
x_values = list(range(2, max_result+1))
# controls the spacing between tick marks on the x-axis
# we need a bar for each of the possible  and we store these in a list called x_values(starts at 1 and ends at the number of sides on the die plotly doesn't accept the results of the range() function directly
# so we convert the range to a list() function
data = [Bar(x=x_values, y=frequencies)]
# The Bar() represents a data set will be formatted as a bar chart
# And the class needs  a list of x_values / y_values
# The class must be wrapped in square backets can have more elements.

x_axis_config = {'title': 'Result', 'dtick': 1}
# x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
# my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
# We put the titles on the variable as well as offline.pot(needs a..
# dictionary containig data and layout objects also accepts a name
# for the file where the graph will be save(d6.html)
