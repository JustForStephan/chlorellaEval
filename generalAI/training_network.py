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

def calc_network(x):
    # calc actual network output
    i1.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][0], iw[1][0], iw[2][0], iw[3][0]])
    i2.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][1], iw[1][1], iw[2][1], iw[3][1]])
    i3.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][2], iw[1][2], iw[2][2], iw[3][2]])
    i4.update([input_light[x], input_co2[x], input_temp[x], 1], [iw[0][3], iw[1][3], iw[2][3], iw[3][3]])
    h1.update([i1.y, i2.y, i3.y, i4.y], [hw[0][0], hw[1][0], hw[2][0], hw[3][0]])
    h2.update([i1.y, i2.y, i3.y, i4.y], [hw[0][1], hw[1][1], hw[2][1], hw[3][1]])
    o.update([h1.y, h2.y], [ow[0], ow[1]])


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
scale_light = 10.0e-5
scale_CO2 = 1.0
scale_temp = 1.0/100
print("finished")

# declare input data
print("- load input data")
input_light = np.dot(read_input("./../input_data.json", "general_regression", "light_intensity"),scale_light)
input_co2 = np.dot(read_input("./../input_data.json", "general_regression", "CO2_proportion"),scale_CO2)
input_temp = np.dot(read_input("./../input_data.json", "general_regression", "ambient_temperature"),scale_temp)
y_data = read_input("./../input_data.json", "general_regression", "CO2_capture_capacity")
print("scaled light: " + str(input_light[5]))
print("scaled CO2-proportion: " + str(input_co2[5]))
print("scaled temperature: " + str(input_temp[5]))
print("finished")

# adapt weights
print("- start training of network")
eta = read_input("./../input_data.json", "general_regression", "eta")
for running_index in range(read_input("./../input_data.json", "general_regression", "running_time_training")):
    for x in range(len(input_temp)):
        calc_network(x)
        print(str(running_index)+":"+str(o.y))

        error = y_data[x] - o.y

        # adaption for output weights
        ow[0] += 2*error*o.y*(1-o.y)*h1.y*eta
        ow[1] += 2*error*o.y*(1-o.y)*h2.y*eta

        # adaption for hidden weights
        hw[0][0] += 2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * i1.y * eta
        hw[0][1] += 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * i1.y * eta
        hw[1][0] += 2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * i2.y * eta
        hw[1][1] += 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * i2.y * eta
        hw[2][0] += 2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * i3.y * eta
        hw[2][1] += 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * i3.y * eta
        hw[3][0] += 2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * i4.y * eta
        hw[3][1] += 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * i4.y * eta

        # adaption for input weights
        iw[0][0] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[0][0] * i1.y * (1-i1.y) * input_light[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[0][1] * i1.y * (1-i1.y) * input_light[x]) * eta
        iw[0][1] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[1][0] * i2.y * (1-i2.y) * input_light[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[1][1] * i2.y * (1-i2.y) * input_light[x]) * eta
        iw[0][2] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[2][0] * i3.y * (1-i2.y) * input_light[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[2][1] * i3.y * (1-i3.y) * input_light[x]) * eta
        iw[0][3] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[3][0] * i4.y * (1-i4.y) * input_light[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[3][1] * i4.y * (1-i4.y) * input_light[x]) * eta

        iw[1][0] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[0][0] * i1.y * (1-i1.y) * input_co2[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[0][1] * i1.y * (1-i1.y) * input_co2[x]) * eta
        iw[1][1] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[1][0] * i2.y * (1-i2.y) * input_co2[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[1][1] * i2.y * (1-i2.y) * input_co2[x]) * eta
        iw[1][2] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[2][0] * i3.y * (1-i3.y) * input_co2[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[2][1] * i3.y * (1-i3.y) * input_co2[x]) * eta
        iw[1][3] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[3][0] * i4.y * (1-i4.y) * input_co2[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[3][1] * i4.y * (1-i4.y) * input_co2[x]) * eta

        iw[2][0] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[0][0] * i1.y * (1-i1.y) * input_temp[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[0][1] * i1.y * (1-i1.y) * input_temp[x]) * eta
        iw[2][1] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[1][0] * i2.y * (1-i2.y) * input_temp[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[1][1] * i2.y * (1-i2.y) * input_temp[x]) * eta
        iw[2][2] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[2][0] * i3.y * (1-i3.y) * input_temp[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[2][1] * i3.y * (1-i3.y) * input_temp[x]) * eta
        iw[2][3] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[3][0] * i4.y * (1-i4.y) * input_temp[x] + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[3][1] * i4.y * (1-i4.y) * input_temp[x]) * eta

        iw[3][0] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[0][0] * i1.y * (1-i1.y) + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[0][1] * i1.y * (1-i1.y)) * eta
        iw[3][1] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[1][0] * i2.y * (1-i2.y) + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[1][1] * i2.y * (1-i2.y)) * eta
        iw[3][2] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[2][0] * i3.y * (1-i3.y) + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[2][1] * i3.y * (1-i3.y)) * eta
        iw[3][3] += (2*error*o.y*(1-o.y) * ow[0] * h1.y * (1-h1.y) * hw[3][0] * i4.y * (1-i4.y) + 2*error*o.y*(1-o.y) * ow[1] * h2.y * (1-h2.y) * hw[3][1] * i4.y * (1-i4.y)) * eta

print("finished")

# calc network output for all given inputs
network_output = []
for x in range(len(input_temp)):
    calc_network(x)
    network_output.append(o.y)
print(network_output)

print("- storage data")
data = {"linear_regression": read_accuracy("linear_regression")}
data.update({"sigmoid_regression": read_accuracy("sigmoid_regression")})
new_data = {"input_light": read_input("./../input_data.json", "general_regression", "light_intensity"), "input_co2": read_input("./../input_data.json", "general_regression", "CO2_proportion"), "input_temp": read_input("./../input_data.json", "general_regression", "ambient_temperature"), "network_capacity": network_output, "natural_capacity": y_data}
data.update({"general_regression": new_data})
write_json("./../accuracy.json", str(data))
print("finished")
