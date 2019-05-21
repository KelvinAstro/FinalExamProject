import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


class Body:
    res = 50
    u = np.linspace(0, 2 * np.pi, res)
    v = np.linspace(0, np.pi, res)

    def __init__(self, distance, radius, angle, color="b"):
        self.distance = distance
        self.radius = radius
        self.angle = angle * np.pi / 180
        self.color = color
        self.x = distance * np.cos(angle)
        self.y = distance * np.sin(angle)
        self.satalites = np.array([], dtype=Body)

    def sphere(self):
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = self.radius * np.outer(np.cos(u), np.sin(v)) + self.x
        y = self.radius * np.outer(np.sin(u), np.sin(v)) + self.y
        z = self.radius * np.outer(np.ones(np.size(u)), np.cos(v))

        return x, y, z

    def creatSatalites(self, sat):
        sat.x += self.x
        sat.y += self.y
        self.satalites = np.append(self.satalites, sat)
