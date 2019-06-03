import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from body import Body
from matplotlib.colors import LightSource


def plot(body):
    x, y, z = body.sphere()
    color = body.color
    li = np.rad2deg(body.angle % (2 * np.pi))
    ls = LightSource(-li - 90, 0)
    ax.plot_surface(x, y, z, color=color, lightsource=ls)
    for sat in body.satellites:
        plot(sat)
    ax.plot3D(body.xp, body.yp, color=color, alpha=0.45)


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

    dim = 10
    ax.set_xlim3d([-dim * 16, dim * 16])
    ax.set_xlabel("X")

    ax.set_ylim3d([-dim * 16, dim * 16])
    ax.set_ylabel("Y")

    ax.set_zlim3d([-dim * 9, dim * 9])
    ax.set_zlabel("Z")

    ax.set_title("Solar System")

    ax.axis("off")


# creating the sun, planets and moon

mercury = Body(
    radius=3, angle=90, distance=15, days=88, color="#6f1520", name="mercury"
)
venus = Body(radius=7, angle=90, distance=40, days=224.7, color="#c46b00", name="venus")

moon = Body(radius=2, angle=90, distance=1, days=30, color="#000000", name="moon")
earth = Body(
    radius=7,
    angle=90,
    distance=76,
    days=365.3,
    color="#0079c4",
    satellites=[moon],
    name="earth",
)

# mars = Body(radius=30, angle=90, distance=66, days=90, color="#9e2111", name="mars")
mars = Body(radius=4, angle=90, distance=106, days=687, color="#9e2111", name="mars")

jupiter = Body(
    radius=12, angle=90, distance=170, days=4331.6, color="#d89741", name="jupiter"
)
saturn = Body(
    radius=10, angle=90, distance=220, days=10759.2, color="#e0c198", name="saturn"
)

sunSats = [mercury, venus, earth, mars, jupiter, saturn]

# sunSats = [mars]


for i in range(5):
    r = np.random.randint(3, 12)
    d = np.random.randint(6, 100)
    s = np.random.randint(3, 12)


sun = Body(20, satellites=sunSats, name="sun")

# Attaching 3D axis to the figure

fig = plt.figure(figsize=(16, 9))
ax = p3.Axes3D(fig, azim=0, elev=0, proj_type="persp")


# Animation

# lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in sun.sa]
ani = animation.FuncAnimation(
    fig, animate, fargs=([sun.satellites]), interval=1, init_func=init
)
animate(0, sun.satellites)

plt.show()
