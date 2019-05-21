import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from body import Body


def plot(body):
    x, y, z = body.sphere()
    color = body.color
    ax.plot_surface(x, y, z, color=color)
    for i in body.satalites:
        plot(i)


# Fixing random state for reproducibility
np.random.seed(14537)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines

# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()

# Setting the axes properties
ax.set_xlim3d([-20.0, 20.0])
ax.set_xlabel("X")

ax.set_ylim3d([-20.0, 20.0])
ax.set_ylabel("Y")

ax.set_zlim3d([-20.0, 20.0])
ax.set_zlabel("Z")

ax.set_title("3D Test")


# Plot the surface

sun = Body(0, 10, 0, "y")
earth = Body(20, 3, 0)
mars = Body(25, 6, 90, "r")

moon = Body(5, 1, 90, "k")

sun.creatSatalites(earth)
sun.creatSatalites(mars)

earth.creatSatalites(moon)

plot(sun)


plt.show()
