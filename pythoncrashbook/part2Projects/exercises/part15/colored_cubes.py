import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)

ax.axis([0, 5001, 0, 5001])

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)
plt.show()
