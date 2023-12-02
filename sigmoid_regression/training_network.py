import json
from neurons import neuron
import numpy as np
import matplotlib.pyplot as mpl

import math

w = np.random.random((5,2))
print(w)

def read_json(file, name):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data[name]

def write_json(name, data):
    f = open(name, "w")
    f.write(estetics_in_json(data))
    f.close()

def estetics_in_json(string):                   # makes the json readable before upload
    string = string.replace("'",'"')
    string = string.replace("],","],\n")
    string = string.replace("{","{\n")
    string = string.replace("}", "\n}")
    string = string.replace(', "',',\n"')
    return string

print("Neural Network gets configurated:")

#declaration of neurons

neuron3 = neuron([1, 1], [w[1][0], w[2][0]])
neuron4 = neuron([1, 1], [w[1][1], w[2][1]])
neuron5 = neuron([neuron3.y, neuron4.y], [w[3][0], w[4][0]])

print("first neuron3: "+str(neuron3.z) + "  " + str(neuron3.y))
print("first neuron4: "+str(neuron4.z) + "  " + str(neuron4.y))
print("first neuron5: "+str(neuron5.z) + "  " + str(neuron5.y))

print("finished\n")

print("input values gets configurated:")

#x = read_json("vectors_new.json", "frequency")
#y = read_json("vectors_new.json", "photosynthetic_activity")
x = np.linspace(0.1,0.9,10)
y = x**3

#for i in range(len(x)):
#    y[i] = float(y[i]*10e5)

print("neural input: " + str(x))
print("neural output: "+ str(y))

print("finished\n")
print("training of neural network:")
eta = read_json("vectors_new.json", "etha")
eta = 0.1
# loop for training index
#for running_index in range(read_json("vectors_new.json", "running_time_training")):
for cycle in range(100000):
    sume = 0.0
    # loop for length of input
    for i in range(len(x)):
        neuron3.update([x[i], 1.0], [w[1][0], w[2][0]])
        neuron4.update([x[i], 1.0], [w[1][1], w[2][1]])
        neuron5.update([neuron3.y, neuron4.y], [w[3][0], w[4][0]])
        e = y[i] - neuron5.y
        w[3][0] += e * neuron5.y * (1.0 - neuron5.y) * neuron3.y * eta # * (1+np.abs(np.power(e,n)))
        w[4][0] += e * neuron5.y * (1.0 - neuron5.y) * neuron4.y * eta # * (1+np.abs(np.power(e,n)))
        w[1][0] += e * neuron5.y * (1.0 - neuron5.y) * w[3][0] * neuron3.y * (1.0 - neuron3.y) * x[i] * eta
        w[1][1] += e * neuron5.y * (1.0 - neuron5.y) * w[4][0] * neuron4.y * (1.0 - neuron4.y) * x[i] * eta
        w[2][0] += e * neuron5.y * (1.0 - neuron5.y) * w[3][0] * neuron3.y * (1.0 - neuron3.y) * eta
        w[2][1] += e * neuron5.y * (1.0 - neuron5.y) * w[4][0] * neuron4.y * (1.0 - neuron4.y) * eta
        sume+= np.abs(e)
        print("\n" + f"t={y[i]} y5={round(neuron5.y, 3)} e={round(e,4)} y3={round(neuron3.y, 3)} w12={w[3][0]} {w[4][0]}")
    print(f"e={round(sume, 4)}")
    new_y = []
    for i in range(len(x)):
        neuron3.update([x[i], 1.0], [w[1][0], w[2][0]])
        neuron4.update([x[i], 1.0], [w[1][1], w[2][1]])
        neuron5.update([neuron3.y, neuron4.y], [w[3][0], w[4][0]])
        new_y.append(neuron5.y)

    plot1 = mpl.plot(x, y)
    plot1 = mpl.plot(x, new_y)
    mpl.show()
    print("neural_output:" + str(neuron5.y))
#    print("error: " + str(e))
#    print("--------------------------------")

#print("finished\n")

print("\nweight 1/0: " + str(w[1][0]) + "   |   weight 1/1: " + str(w[1][1]))
print("weight 2/0:" + str(w[2][0]) + "   |   weight 2/1:" + str(w[2][1]))
print("weight 3/0:" + str(w[3][0]) + "   |   weight 4/0:" + str(w[4][0]))

#print("safe neural configuration of weights:")
#data = str({"weight1/0":w[1][0], "weight1/1": w[1][1], "weight2/0": w[2][0], "weight2/1": w[2][1], "weight3":w[3][0], "weight4": w[4][0], "etha": read_json("vectors_new.json", "etha"), "running_index": read_json("vectors_new.json", "running_time_training")})#write_json("neural_config.json", data)
#write_json("neural_config.json", data)
#print("finished\n")

print("performe test:")
# test neural network
new_y = []
for i in range(len(x)):
    neuron3.update([x[i], 1.0], [w[1][0], w[2][0]])
    neuron4.update([x[i], 1.0], [w[1][1], w[2][1]])
    neuron5.update([neuron3.y, neuron4.y], [w[3][0], w[4][0]])
    new_y.append(neuron5.y)

#print(read_json("vectors_new.json", "photosynthetic_activity"))
print(y)
print(new_y)
print("finished\n")

#print("safe test data for mathematical depiction")
#data = {"linear_regression": read_json("./../accuracy.json", "linear_regression")}
#data.update({"sigmoid_regression": {"photosynthetic_activity_calc":new_y}})
#write_json("./../accuracy.json", str(data))
#print("finished\n")

