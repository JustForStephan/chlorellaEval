import numpy as np
from neurons import neuron
import json

def read_input(file, key, subkey):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data[key][subkey]

def read_accuracy(file, key):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data[key]

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

# declare neurons
i1 = neuron(); i2 = neuron(); i3 = neuron(); i4 = neuron(); h1 = neuron(); h2 = neuron(); o = neuron()

# declace weights
iw = np.random.random((4, 4))
hw = np.random.random((4, 2))

# declare scale factor
scale_light = 10e2
scale_CO2 = 1
scale_temp = 0.1

# declare input data
input_light = np.dot(read_input("./../input_data.json", "general_regression", "light_intensity"),scale_light)
input_co2 = np.dot(read_input("./../input_data.json", "general_regression", "CO2_proportion"),scale_CO2)
input_temp = np.dot(read_input("./../input_data.json", "general_regression", "ambient_temperature"),scale_temp)

# adapt weights

for running_index in range(read_input("./../input_data.json", "general_regression", "running_time_training")):
    for value in range(len(input_temp)):
        pass

