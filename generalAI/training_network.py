import numpy as np
from neurons import neuron
import json

def read_input(file, key, subkey):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data[key][subkey]

def read_accuracy(key):
    f = open("./../accuracy.json", "r")
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
ow = np.random.random((2, 1))

# declare scale factor
print("- define scale factors")
scale_light = 10e-5
scale_CO2 = 1
scale_temp = 1/100
print("finished")

# declare input data
print("- load input data")
input_light = np.dot(read_input("./../input_data.json", "general_regression", "light_intensity"),scale_light)
input_co2 = np.dot(read_input("./../input_data.json", "general_regression", "CO2_proportion"),scale_CO2)
input_temp = np.dot(read_input("./../input_data.json", "general_regression", "ambient_temperature"),scale_temp)
print("scaled light: " + str(input_light[5]))
print("scaled CO2-proportion: " + str(input_co2[5]))
print("scaled temperature: " + str(input_temp[5]))
print("finished")

# adapt weights
print("- start training of network")
eta = read_input("./../input_data.json", "general_regression", "eta")
for running_index in range(read_input("./../input_data.json", "general_regression", "running_time_training")):
    for x in range(len(input_temp)):

        # calc actual network output
        i1.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][0], iw[1][0], iw[2][0], iw[3][0]])
        i2.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][1], iw[1][1], iw[2][1], iw[3][1]])
        i3.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][2], iw[1][2], iw[2][2], iw[3][2]])
        i4.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][3], iw[1][3], iw[2][3], iw[3][3]])
        h1.update([i1.y, i2.y, i3.y, i4.y], [hw[0][0], hw[1][0], hw[2][0], hw[3][0]])
        h2.update([i1.y, i2.y, i3.y, i4.y], [hw[0][1], hw[1][1], hw[2][1], hw[3][1]])
        o.update([h1.y, h2.y],[ow[0], ow[1]])
        print(o.y)
print("finished")

print("- storage data")
old_data = read_accuracy("linear_regression")
old_data.update(read_accuracy("sigmoid_regression"))
#new_data = "general_regression": {"calc_co2_capture_capacity": calc_data}
print("finished")
