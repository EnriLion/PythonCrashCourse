# import matplotlib.pyplot as plt
# import random

# class RandomWalk:
#     def __init__(self, x0, y0, n):
#         self.x0 = x0
#         self.y0 = y0
#         self.n = n
#         self.x_values = [x0]
#         self.y_values = [y0]

#     def simulate(self):
#         for i in range(self.n):
#             dx = random.choice([-1, 1])
#             dy = random.choice([-1, 1])
#             self.x_values.append(self.x_values[-1] + dx)
#             self.y_values.append(self.y_values[-1] + dy)

# if __name__ == '__main__':
#     rw = RandomWalk(0, 0, 5000)
#     rw.simulate()

#     # Plot the random walk path
#     plt.plot(rw.x_values, rw.y_values, linewidth=0.5)

#     # Set the labels and title
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.title('Path of a pollen grain on the surface of a drop of water')

#     # Show the plot
#     plt.show()

