import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    # rw = RandomWalk()
    rw = RandomWalk(5000)
    # Importing the RandomWalk store it in rw
    rw.fill_walk()
    # we call fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi=128)
    # dpi set a plot size that makes effective use of the space available
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # We use range()=generate list of number equal to numbepoints in the walk.

    # ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # we feed the walk's x-and y-values to scatter
    # we pass point_numbers to the c argument, use the Blues colormap
    # the result is a varies from light to dark blue along a gradient
    # Remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
