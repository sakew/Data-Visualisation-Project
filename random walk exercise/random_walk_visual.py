import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.

# Keep making new walks, as long as program is active.
while True:


    random_walk = RandomWalk()

    random_walk = RandomWalk(5000)
    random_walk.fill_walk()

    # Set the size of the plotting window.
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(random_walk.num_points))
    plt.scatter(random_walk.x_values, random_walk.y_values,
                c = point_numbers, cmap= plt.cm.Blues, edgecolors="none", s = 15)



    # Emphasizing the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='red', edgecolors='none', s=100)







    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break