import numpy as np
import matplotlib.pyplot as plt

class Representation:
    def __init__(self, start_point=0.0, end_point=2.0, scale_rate=0.01, x_label="", y_label="", title="", grid=True):
        self.start_point = start_point
        self.end_point = end_point
        self.scale_rate = scale_rate
        self.x_label = x_label
        self.y_label = y_label
        self.title = title
        self.grid = grid
        t = np.arange(self.start_point, self.end_point, self.scale_rate)
        s = 1 + np.sin(2*np.pi*t)
        plt.plot(t, s)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.grid)
    def show(self):
        plt.show()
    def save(self, filename):
        plt.savefig(filename)

a = Representation(x_label="Time (s)", y_label="Volts (Vm)", title="Pollometro xd")

a.show()

a.save("polla.png")