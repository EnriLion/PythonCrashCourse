
import  matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
# this code genetates a plot in a wide varitey of styles available

fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)
ax.plot(input_values, squares, linewidth=3)
# the thickness of the line that plot() generates

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
# The set_title method sets a title for the chart
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=24)

# The methods allow you to set a title for each of the axes

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)
# The method tick_params() styles the tick marks

plt.show()

