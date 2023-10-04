import matplotlib.pyplot as plt

from die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values,  s=10)

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)

ax.axis([0, 5100, 0, 5100**3])

plt.show()
