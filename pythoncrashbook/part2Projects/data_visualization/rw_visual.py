import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
# Importing the RandomWalk store it in rw
rw.fill_walk()
# we call fill_walk()

# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
# we feed the walk's x-and y-values to scatter
plt.show()
