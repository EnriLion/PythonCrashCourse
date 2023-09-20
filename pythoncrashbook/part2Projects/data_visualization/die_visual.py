from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6
die = Die()
# we create  an instace of Die with the default six sides

# Make some rolls, and store results in a list.
results = []
for roll_num in range(100):
    # We roll the die 100 times and store each roll in th elist results
    # We're not longer printing the results, we can increase the number of stimulated rolls to 1000
    result = die.roll()
    results.append(result)

# print(results)
# Analyze the results.
frequencies = []
# To analyze the rolls, we create the empty list frequencies
for value in range(1, die.num_sides+1):
    # We loop through the possible values(1 thorugh 6)
    frequency = results.count(value)
    # how many times each number appears in results
    frequencies.append(frequency)
    # And then append this value to the frequencies list
# print(frequencies)

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
