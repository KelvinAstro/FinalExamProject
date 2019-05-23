import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from body import Body


def plot(body):
    x, y, z = body.sphere()
    color = body.color
#     ax.plot_surface(x, y, z, color=color)
    ax.scatter(body.x, body.y, zs=0, zdir="y", c=color, label="points in (x,z)")
    for i in body.satellites:
        plot(i)


def animate(angle, bodys):
    for body in bodys:
        body.move(angle)
        plot(body)
        print(body, body.angle * 180 / np.pi)


# Fixing random state for reproducibility
np.random.seed(14537)


# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig, azim=90, elev=0, proj_type="ortho")

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


# creating the sun, planets and moon
moon = Body(1, 90, 10, "k")
earthSats = [moon]
sun = Body(10)
earth = Body(3, 90, 20, satellites=earthSats, color="b")
mars = Body(6, 90, 25, "r")


sun.creatSatellites([earth])
sun.creatSatellites([mars])


# Plot the surface

plot(sun)
x = 1
planets = [[earth, mars]]
ani = animation.FuncAnimation(fig, animate, [5], fargs=(planets), interval=10)

print(earth.x, earth.y)
print(moon.x, moon.y)
print(np.sqrt(np.square(earth.x - moon.x) + np.square(earth.y - moon.y)))
print((np.arctan((earth.y - moon.y) / (earth.x - moon.x)) * 180 / np.pi))

plt.show()

