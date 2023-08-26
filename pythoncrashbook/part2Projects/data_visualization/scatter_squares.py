import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
x_values = range(1, 1001)
# y_values = [1, 4, 9, 16, 25]
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(5, 10, s=200)# we call scatter() and use the s argument to set the size of the dots used to draw the graph. When we run scatter_sqares we should see a single point in the middle of the chart.

ax.scatter(x_values, y_values, s=10)

# Set chart title and lable axes.

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
#Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()
