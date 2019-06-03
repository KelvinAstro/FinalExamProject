import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib.colors import LightSource


class Body:
    def __init__(
        self, radius, angle=0, distance=0, days=1, color="y", satellites=None, name=str
    ):
        """Class for creating a celestial body and its satellites (e.g., the sun, planets, moons). 
        radius: the radius of the body
        angle: the angle around the orgin of the graph.

        distance: the distace the body is from its parent. Zero if it has no parent (e.g. the sun).

        orbit: earth days to complete an orbit
        
        color: the body's color. rgb in range [0, 1]; hex string; 
        {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}; or any othe matplotlib formats

        satellites: a list filled with Body objects. The items in the list are
        the sataliltes of this body. The suns satellites would be considered the planets 
        and asteroids that orbit it.
        """

        self.radius = radius
        self.angle = np.deg2rad(angle)
        self.distance = distance
        self.days = days
        self.color = color
        self.x = distance * np.cos(np.radians(angle))
        self.y = distance * np.sin(np.radians(angle))
        self.z = 0
        self.angularSpeed = 2 * np.pi / days
        self.xp, self.yp = [], []
        self.name = name

        if satellites is None:
            self.satellites = np.array([], dtype=Body)
        else:
            satellites = self.satTranslate(satellites)
            self.satellites = np.array(satellites)

        res = 15
        self.u = np.linspace(0, 2 * np.pi, res)
        self.v = np.linspace(0, np.pi, res)

        self.sx = self.radius * np.outer(np.cos(self.u), np.sin(self.v)) 
        self.sy = self.radius * np.outer(np.sin(self.u), np.sin(self.v)) 
        self.sz = (self.radius) * np.outer(np.ones(np.size(self.u)), np.cos(self.v))

    def satTranslate(self, satList):
        for sat in satList:
            sat.angularSpeed += self.angularSpeed
            sat.distance += self.radius
            sat.x = (sat.distance) * np.cos(sat.angle + self.angle) + self.x
            sat.y = (sat.distance) * np.sin(sat.angle + self.angle) + self.y
        return satList

    def sphere(self):
        return self.sx + self.x, self.sy + self.y, self.sz + self.z

    def creatSatellites(self, satList):
        satList = self.satTranslate(satList)
        self.satellites = np.append(self.satellites, satList)

    def orbit(self, angle=0, x=0, y=0, r=0):
        self.angle += self.angularSpeed
        self.x = (self.distance + r) * np.cos(self.angle) + x
        self.y = (self.distance + r) * np.sin(self.angle) + y
        self.xp.append(self.x)
        self.yp.append(self.y)
        if len(self.xp) == round(self.days / 3) and self.name != "moon":
            del self.xp[0]
            del self.yp[0]
        if self.name == "moon" and len(self.xp) == round(self.days * 2):
            del self.xp[0]
            del self.yp[0]

        for sat in self.satellites:
            sat.orbit(self.angle, self.x, self.y, self.radius)

    def __repr__(self):
        return "Planet: {}".format(self.name)


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

mars = Body(radius=4, angle=90, distance=106, days=687, color="#9e2111", name="mars")

jupiter = Body(
    radius=12, angle=90, distance=170, days=4331.6, color="#d89741", name="jupiter"
)
saturn = Body(
    radius=10, angle=90, distance=220, days=10759.2, color="#e0c198", name="saturn"
)

sunSats = [mercury, venus, earth, mars, jupiter, saturn]


sun = Body(20, satellites=sunSats, name="sun")

# Attaching 3D axis to the figure

fig = plt.figure(figsize=(16, 9))
ax = p3.Axes3D(fig, azim=0, elev=0, proj_type="persp")


# Animation
ani = animation.FuncAnimation(
    fig, animate, fargs=([sun.satellites]), interval=1, init_func=init
)


plt.show()
