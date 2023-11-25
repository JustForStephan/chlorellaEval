import random
import numpy

class neuron:

    position = "input_neuron"
    weight = random.random()
    z = 0
    y = 0
    x = []
    w = []
    def __init__(self, x, w):
        self.z = self.calc_z(x,w)
        self.y = self.calc_y(self.z)

    def calc_z(self, x, w):
        z = numpy.dot(x,w)
        if z.shape != (): z = z[0]
        return z

    def calc_y(self, z):
        return 1/(1+numpy.exp((-1)*z))
