import math

class neuron:

    z = 0
    y = 0

    def __init__(self, x, w):
        self.z = self.calc_z(x,w)
        self.y = self.calc_y(self.z)

    def calc_z(self, x, w):
        z = 0
        for i in range(len(x)):
            z += float(x[i])*float(w[i])
        return z

    def calc_y(self, z):
        return (1/(1+math.exp((-1)*z)))

    def update(self, x, w):
        self.z = self.calc_z(x, w)
        self.y = self.calc_y(self.z)

class neuronOutput():

    y = 0

    def __init__(self, x, w):
        self.y = self.calc_y(x,w)

    def calc_y(self, x, w):
        y = 0
        for i in range(len(x)):
            y += float(x[i])*float(w[i])
        return y

    def update(self, x, w):
        self.y = self.calc_y(x, w)
