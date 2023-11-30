import json
from neurons import neuron
from neurons import neuronOutput
import random
import math

w = [
    [1,1],
    [random.random(), random.random()],
    [random.random(), random.random()],
    random.random(),
    random.random()
]

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
neuron1 = neuron([1], [w[1][0]])
neuron2 = neuron([1], [w[1][1]])
neuron3 = neuron([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
neuron4 = neuron([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
neuron5 = neuron([neuron3.y, neuron4.y], [w[3], w[4]])

print("finished\n")

print("input values gets configurated")
x = read_json("vectors_new.json", "frequency")
for a in x:
    a = a/math.pow(10,8)
print("finished\n")

print("training of neural network:")

# loop for training index
for running_index in range(read_json("vectors_new.json", "running_time_training")):

#    print("\nweight 1/0: " + str(w[1][0]) + "   |   weight 1/1: " + str(w[1][1]))
#    print("weight 1/0:" + str(w[2][0]) + "   |   weight 1/1:" + str(w[2][1]))
#    print("weight 3/0:" + str(w[3]) + "   |   weight 4/0:" + str(w[4]))

    # loop for length of input
    for i in range(len(x)):
        neuron1.update([x[i]], [w[1][0]])
        neuron2.update([1], [w[1][1]])
        neuron3.update([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
        neuron4.update([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
        neuron5.update([neuron3.y, neuron4.y], [w[3], w[4]])
        e = read_json("vectors_new.json", "photosynthetic_activity")[i] - neuron5.y

        w[3] += 2 * e * neuron5.z * (1 - neuron5.z) * neuron3.y * read_json("vectors_new.json","etha")
        w[4] += 2 * e * neuron5.z * (1 - neuron5.z) * neuron4.y * read_json("vectors_new.json","etha")
        w[1][0] += 2 * e * neuron5.z * (1 - neuron5.z) * w[3] * neuron3.z * (1 - neuron3.z) * neuron1.y * read_json("vectors_new.json","etha")
        w[1][1] += 2 * e * neuron5.z * (1 - neuron5.z) * w[4] * neuron4.z * (1 - neuron4.z) * neuron1.y * read_json("vectors_new.json","etha")
        w[2][0] += 2 * e * neuron5.z * (1 - neuron5.z) * w[3] * neuron3.z * (1 - neuron3.z) * neuron2.y * read_json("vectors_new.json","etha")
        w[2][1] += 2 * e * neuron5.z * (1 - neuron5.z) * w[4] * neuron4.z * (1 - neuron4.z) * neuron2.y * read_json("vectors_new.json","etha")

print("finished\n")
print("safe neural configuration of weights")
data = str({"weight1/0":w[1][0], "weight1/1": w[1][1], "weight2/0": w[2][0], "weight2/1": w[2][1], "weight3":w[3], "weight4": w[4], "etha": read_json("vectors_new.json", "etha"), "running_index": read_json("vectors_new.json", "running_time_training")})#write_json("neural_config.json", data)
print("finished\n")

print("performe test:")
# test neural network
new_y = []
for i in range(len(x)):
    neuron1.update([x[i]], [w[1][0]])
    neuron2.update([1], [w[1][1]])
    neuron3.update([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
    neuron4.update([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
    neuron5.update([neuron3.y, neuron4.y], [w[3], w[4]])
    new_y.append(neuron5.y)

print(read_json("vectors_new.json", "photosynthetic_activity"))
print(new_y)
print("finished\n")

print("safe test data for mathematical depiction")
data = {"linear_regression": read_json("./../accuracy.json", "linear_regression")}
data.update({"sigmoid_regression": {"photosynthetic_activity_calc":new_y}})
write_json("./../accuracy.json", str(data))
print("finished\n")