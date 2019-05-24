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
        body.orbit(np.rad2deg(body.angularSpeed))
        plot(body)


def init():
    # Setting the axes properties
    ax.clear()
    x, y, z = sun.sphere()
    color = sun.color
    ax.plot_surface(x, y, z, color=color)
    dim = 40
    ax.set_xlim3d([-dim, dim])
    ax.set_xlabel("X")

    ax.set_ylim3d([-dim, dim])
    ax.set_ylabel("Y")

    ax.set_zlim3d([-5, 5])
    ax.set_zlabel("Z")

    ax.set_title("3D Test")


# creating the sun, planets and moon
moon = Body(1, 90, 10, 28, color="k")
earthSats = [moon]

sun = Body(10)
mercury = Body(3, 90, 10, 88, color="#6f1520")
venus = Body(3, 90, 15, 224.7, color="#c46b00")
earth = Body(3, 90, 20, 365.3, satellites=earthSats, color="#0079c4")
mars = Body(3, 90, 25, 687, color="#9e2111")
jupiter = Body(3, 90, 4331.6, color="#d89741")
saturn = Body(3,90,30, 10759.2, color="#e0c198")

sunSats = [mercury, venus, earth, mars, jupiter, saturn]
sun.creatSatellites(sunSats)



# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig, azim=90, elev=0, proj_type="persp")


# Animation

ani = animation.FuncAnimation(
    fig, animate, [5], fargs=([sun.satellites]), interval=1
)

plt.show()
