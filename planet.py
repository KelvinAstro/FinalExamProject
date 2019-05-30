import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from body import Body


def plot(body):
    x, y, z = body.sphere()
    color = body.color
    ax.plot_surface(x, y, z, color=color)
    for sat in body.satellites:
        plot(sat)


def animate(angle, bodys):
    init()
    for body in bodys:
        body.orbit()
        plot(body)


def init():
    # Setting the axes properties
    ax.clear()
    x, y, z = sun.sphere()
    color = sun.color
    ax.plot_surface(x, y, z, color=color)
    dim = 150
    ax.set_xlim3d([-dim, dim])
    ax.set_xlabel("X")

    ax.set_ylim3d([-dim, dim])
    ax.set_ylabel("Y")

    ax.set_zlim3d([-dim, dim])
    ax.set_zlabel("Z")

    ax.set_title("3D Test")


# creating the sun, planets and moon

mercury = Body(radius=2, angle=90, distance=5, days=88, color="#6f1520")
venus = Body(radius=6, angle=90, distance=20, days=224.7, color="#c46b00")

moon = Body(radius=2, angle=90, distance=1, days=30, color="#000000")
earth = Body(
    radius=6, angle=90, distance=46, days=365.3, color="#0079c4", satellites=[moon]
)

mars = Body(radius=3, angle=90, distance=66, days=687, color="#9e2111")
jupiter = Body(radius=10, angle=90, distance=100, days=4331.6, color="#d89741")
saturn = Body(radius=9, angle=90, distance=130, days=10759.2, color="#e0c198")

sunSats = [mercury, venus, earth, mars, jupiter, saturn]

sun = Body(20, satellites=sunSats)

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig, azim=0, elev=90, proj_type="persp")

# Animation

ani = animation.FuncAnimation(fig, animate, fargs=([sun.satellites]), interval=1)
# animate(0, sun.satellites)

plt.show()
