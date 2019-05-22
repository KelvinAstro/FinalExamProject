import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class Body:
    res = 40
    u = np.linspace(0, 2 * np.pi, res)
    v = np.linspace(0, np.pi, res)

    def __init__(self, radius, angle=0, distance=0, color="y", satellites=None):
        """Class for creating a celestial body and its satellites (e.g., the sun, planets, moons). 
        radius: the radius of the body
        angle: the angle around the orgin of the graph.

        distance: the distace the body is from its parent. Zero if it has no parent (e.g. the sun).
        
        color: the body's color. rgb in range [0, 1]; hex string; 
        {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}; or any othe matplotlib formats

        satellites: a list filled with Body objects. The items in the list are
        the sataliltes of this body. The suns satellites would be considered the planets 
        and asteroids that orbit it.
        """
        self.distance = distance
        self.radius = radius
        self.angle = angle * np.pi / 180
        self.color = color
        self.x = distance * np.cos(angle)
        self.y = distance * np.sin(angle)

        if satellites is None:
            self.satellites = np.array([], dtype=Body)
        else:
            for sat in satellites:
                sat.x += self.x
                sat.y += self.y
            self.satellites = np.array(satellites)

    def sphere(self):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = self.radius * np.outer(np.cos(u), np.sin(v)) + self.x
        y = self.radius * np.outer(np.sin(u), np.sin(v)) + self.y
        z = self.radius * np.outer(np.ones(np.size(u)), np.cos(v))

        return x, y, z

    def creatSatellites(self, sat):
        sat.x += self.x
        sat.y += self.y
        self.satellites = np.append(self.satellites, sat)

    @angle setter
    def angle(self):
        

