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
    # plt.style.use('classic')
    plt.figure(dpi=128, figsize=(10, 6))
    # dpi set a plot size that makes effective use of the space available
    # point_numbers = range(rw.num_points)
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    # We use range()=generate list of number equal to numbepoints in the walk.

    # ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.scatter(0, 0, c='green', edgecolor='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=75)
    # we feed the walk's x-and y-values to scatter
    # we pass point_numbers to the c argument, use the Blues colormap
    # the result is a varies from light to dark blue along a gradient
    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
