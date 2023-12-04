import json
from neurons import neuron
import numpy as np
import matplotlib.pyplot as mpl

w_frequency = np.random.random((5,2))
w_current = np.random.random((5,2))

scale_factor_x_frequency = 10e-2
scale_factor_x_current = 10e2
scale_factor_y = 10e5

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

# training with specific dataset
def neural_network_training(x, y, w):

    print("Neural Network gets configurated:")

    # declaration of neurons
    neuron3 = neuron([1, 1], [w[1][0], w[2][0]])
    neuron4 = neuron([1, 1], [w[1][1], w[2][1]])
    neuron5 = neuron([neuron3.y, neuron4.y], [w[3][0], w[4][0]])

    print("first neuron3: " + str(neuron3.z) + "  " + str(neuron3.y))
    print("first neuron4: " + str(neuron4.z) + "  " + str(neuron4.y))
    print("first neuron5: " + str(neuron5.z) + "  " + str(neuron5.y))

    print("finished\n")

    print("neural input: " + str(x))
    print("neural output: " + str(y))

    print("training of neural network:")

    # loop for training index
    for running_index in range(read_json("vectors_new.json", "running_time_training")):

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
        print("neural_output:" + str(neuron5.y))
    print("finished\n")
    return w

def print_properties(name, w, scale_factor_x):
    print("Mathematical properties of network: " + name)
    print("\nweight 1/0: " + str(w[1][0]) + "   |   weight 1/1: " + str(w[1][1]))
    print("weight 2/0:" + str(w[2][0]) + "   |   weight 2/1:" + str(w[2][1]))
    print("weight 3/0:" + str(w[3][0]) + "   |   weight 4/0:" + str(w[4][0]))
    print("\neta: " + str(eta)+ "   |   running_index: " + str(read_json("vectors_new.json", "running_time_training")))
    print("input_scale: "+ str(scale_factor_x) + "  |   output_scale: " + str(scale_factor_y))
    print("finished\n")

# test neural network
def test_network(x, w):

    print("performe test:")
    neuron3 = neuron([1, 1], [w[1][0], w[2][0]])
    neuron4 = neuron([1, 1], [w[1][1], w[2][1]])
    neuron5 = neuron([neuron3.y, neuron4.y], [w[3][0], w[4][0]])
    new_y = []
    for i in range(len(x)):
        neuron3.update([x[i], 1.0], [w[1][0], w[2][0]])
        neuron4.update([x[i], 1.0], [w[1][1], w[2][1]])
        neuron5.update([neuron3.y, neuron4.y], [w[3][0], w[4][0]])
        new_y.append(neuron5.y/scale_factor_y)
    return new_y

print("input values gets configurated:")

eta = read_json("vectors_new.json", "etha")
x_frequency = read_json("vectors_new.json", "frequency")
y_frequency = read_json("vectors_new.json", "photosynthetic_activity")
x_current = read_json("vectors_new.json", "input_current")
y_current = read_json("vectors_new.json", "photosynthetic_activity_by_input_current")

for i in range(len(x_frequency)):
    x_frequency[i] = float(x_frequency[i] * scale_factor_x_frequency)
    y_frequency[i] = float(y_frequency[i] * scale_factor_y)
for i in range(len(x_current)):
    x_current[i] = float(x_current[i]*scale_factor_x_current)
    y_current[i] = float(y_current[i]*scale_factor_y)
print("finished\n")

# Calculating the neural network weights for current and for frequency

print("---------------------------------")
print("|CURRENT CALCULATION IS STARTING|")
print("---------------------------------")
w_current = neural_network_training(x_current, y_current, w_current)
print("-----------------------------------")
print("|FREQUENCY CALCULATION IS STARTING|")
print("-----------------------------------")
w_frequency = neural_network_training(x_frequency, y_frequency, w_frequency)

#Printing properties of network
print_properties("current", w_current, scale_factor_x_current)
print_properties("frequency", w_frequency, scale_factor_x_frequency)

print("safe neural configuration of network:")
data_current = str({"current": {"weight1/0":w_current[1][0], "weight1/1": w_current[1][1], "weight2/0": w_current[2][0], "weight2/1": w_current[2][1], "weight3":w_current[3][0], "weight4": w_current[4][0], "etha": read_json("vectors_new.json", "etha"), "running_index": read_json("vectors_new.json", "running_time_training"), "scale_factor_x": scale_factor_x_current, "scale_factor_y": scale_factor_y}})
data_frequency = str({"frequency":{"weight1/0":w_frequency[1][0], "weight1/1": w_frequency[1][1], "weight2/0": w_frequency[2][0], "weight2/1": w_frequency[2][1], "weight3":w_frequency[3][0], "weight4": w_frequency[4][0], "etha": read_json("vectors_new.json", "etha"), "running_index": read_json("vectors_new.json", "running_time_training"), "scale_factor_x": scale_factor_x_frequency, "scale_factor_y": scale_factor_y}})
data = data_current + data_frequency
write_json("neural_config.json", str(data))
print("finished\n")

#testing network
new_currents = test_network(x_current, w_current)
new_frequencies = test_network(x_frequency, w_frequency)

print("real frequency based activity:")
print(read_json("vectors_new.json", "photosynthetic_activity"))
print("calculated frequency based activtiy:")
print(str(new_frequencies))
print("\nreal current based activity:")
print(read_json("vectors_new.json", "photosynthetic_activity_by_input_current"))
print("calculated current based activity:")
print(str(new_currents))
print("finished\n")

# convert data back to original scale
print("Convert data back")
for i in range(len(x_frequency)):
    x_frequency[i] = x_frequency[i]/scale_factor_x_frequency
    y_frequency[i] = y_frequency[i]/scale_factor_y
for i in range(len(x_current)):
    x_current[i] = x_current[i]/scale_factor_x_current
    y_current[i] = y_current[i]/scale_factor_y
print("finished\n")

print("Safe test data for mathematical depiction")
data = {"linear_regression": read_json("./../accuracy.json", "linear_regression")}
data.update({"sigmoid_regression": {"photosynthetic_activity_calc_current":y_current, "photosynthetic_activity_calc_frequency": y_frequency}})
write_json("./../accuracy.json", str(data))
print("finished\n")

mpl.plot(read_json("vectors_new.json", "frequency"), read_json("vectors_new.json", "photosynthetic_activity"))
mpl.plot(read_json("vectors_new.json", "frequency"), y_frequency)
mpl.show()
mpl.plot(read_json("vectors_new.json", "input_current"), read_json("vectors_new.json", "photosynthetic_activity_by_input_current"))
mpl.plot(read_json("vectors_new.json", "input_current"), y_current)
mpl.show()