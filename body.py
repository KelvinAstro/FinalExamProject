import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class Body:
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
        self.radius = radius/10
        self.angle = angle 
        self.color = color
        self.x = distance * np.cos(np.radians(angle))
        self.y = distance * np.sin(np.radians(angle))

        if satellites is None:
            self.satellites = np.array([], dtype=Body)
        else:
            for sat in satellites:
                sat.x = sat.distance * np.cos(np.radians(sat.angle) + np.radians(self.angle)) + self.x
                sat.y = sat.distance * np.sin(np.radians(sat.angle) + np.radians(self.angle)) + self.y
            self.satellites = np.array(satellites)

        res = 10
        self.u = np.linspace(0, 2 * np.pi, res)
        self.v = np.linspace(0, np.pi, res)

    def sphere(self):
        x = self.radius * np.outer(np.cos(self.u), np.sin(self.v)) + self.x
        y = self.radius * np.outer(np.sin(self.u), np.sin(self.v)) + self.y
        z = self.radius * np.outer(np.ones(np.size(self.u)), np.cos(self.v))

        return x, y, z

    def creatSatellites(self, satList):
        for sat in satList:
            sat.x = sat.distance * np.cos(np.radians(sat.angle)  + np.radians(self.angle)) + self.x
            sat.y = sat.distance * np.sin(np.radians(sat.angle)  + np.radians(self.angle)) + self.y
        self.satellites = np.append(self.satellites, satList)

    def move(self, angle):
        print("ok")
        self.angle += angle 
        oldX, oldY = self.x, self.y
        self.x = self.distance * np.cos(np.radians(self.angle))
        self.y = self.distance * np.sin(np.radians(self.angle))
        for sat in self.satellites:
            sat.x += self.x - oldX
            sat.y += self.y - oldY



