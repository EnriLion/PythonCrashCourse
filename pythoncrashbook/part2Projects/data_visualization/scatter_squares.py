import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
x_values = range(1, 1001)
# y_values = [1, 4, 9, 16, 25]
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(5, 10, s=200)# we call scatter() and use the s argument to set the size of the dots used to draw the graph. When we run scatter_sqares we should see a single point in the middle of the chart.

# Defining custom colors
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

#Using a colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# yo can se all the colormaps available in pytplot http://matplotlib.org/;go to Examples, scroll down to Control and click Colormap reference

# Values closer to 0 produce dark colors, and values closer to 1 prouce lighter colors.


# Set chart title and lable axes.

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()

# Saving your plots automatically

plt.savefig('squares_plot.png', bbox_inches='tight')
