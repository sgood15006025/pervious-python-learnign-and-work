import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as program is active
while True:
    # Make a random walk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize = (15, 9))
    point_nuumbers = range( rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3,)

    plt.show()

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    keep_running = input("Make another walk? (y/n) :  ")
    if keep_running == 'n':
        break