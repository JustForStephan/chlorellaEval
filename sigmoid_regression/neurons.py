import math

class neuron:

    z = 0
    y = 0

    def __init__(self, x, w):
        self.z = None
        self.y = None

    def calc_z(self, x, w):
        self.z = 0
        for i in range(len(x)):
            self.z += float(x[i])*float(w[i])

    def calc_y(self):
        self.y=1.0/(1.0+math.exp(-(self.z-0)))
        return self.y

    def update(self, x, w):
        self.calc_z(x, w)
        self.calc_y()