# Create a simulation showing what happens when you
# roll two eight-sided dice 1000 times. Try to picture
# what you think the visualization will look like 
# intuition was correct. Gradually increase the number
# of rolls until you start to see the limits of your
# system's capabilites

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list
results = []
# for roll_num in range(100_00_000):
for roll_num in range(18):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        if result >= 3 and result <= 18:
            results.append(result)
        else:
            break

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a three D6 18 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
