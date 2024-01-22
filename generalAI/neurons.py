import numpy as np

class neuron:

    def __init__(self):
        self.z = None
        self.y = None

    def calc_z(self, x, w):
        self.z = 0.0
        for i in range(len(x)):
            self.z += float(x[i])*float(w[i])

    def calc_y(self):
        self.y=1.0/(1.0+ np.e**(-self.z))
        return self.y

    def update(self, x, w):
        self.calc_z(x, w)
        self.calc_y()