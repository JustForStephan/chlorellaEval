import json
from neurons import neuron
from neurons import neuronOutput
import random

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
    return data[name]

print("Neural Network gets configurated:")

#declaration of neurons
neuron1 = neuron([1], [w[1][0]])
neuron2 = neuron([1], [w[1][1]])
neuron3 = neuron([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
neuron4 = neuron([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
neuron5 = neuronOutput([neuron3.y, neuron4.y], [w[3], w[4]])

print("finished\n")
print("training of neural network:")

# loop for training index
for running_index in range(read_json("vectors_new.json", "running_time_training")):

    print("\nweight 1/0: " + str(w[1][0]) + "   |   weight 1/1: " + str(w[1][1]))
    print("weight 1/0:" + str(w[2][0]) + "   |   weight 1/1:" + str(w[2][1]))
    print("weight 3/0:" + str(w[3]) + "   |   weight 4/0:" + str(w[4]))

    # loop for length of input
    for i in range(len(read_json("vectors_new.json", "frequency"))):
        neuron1.update([read_json("vectors_new.json","frequency")[i]], [w[1][0]])
        neuron2.update([1], [w[1][1]])
        neuron3.update([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
        neuron4.update([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
        neuron5.update([neuron3.y, neuron4.y], [w[3], w[4]])
        e = read_json("vectors_new.json", "photosynthetic_activity")[i] - neuron5.y

        w[3] += 2 * e * neuron3.y * read_json("vectors_new.json","etha")
        w[4] += 2 * e * neuron4.y * read_json("vectors_new.json","etha")
        w[1][0] += 2 * e * w[3] * neuron3.z * (1 - neuron3.z) * neuron1.y * read_json("vectors_new.json","etha")
        w[1][1] += 2 * e * w[4] * neuron4.z * (1 - neuron4.z) * neuron1.y * read_json("vectors_new.json","etha")
        w[2][0] += 2 * e * w[3] * neuron3.z * (1 - neuron3.z) * neuron2.y * read_json("vectors_new.json","etha")
        w[2][1] += 2 * e * w[4] * neuron4.z * (1 - neuron4.z) * neuron2.y * read_json("vectors_new.json","etha")

print("finished\n")
print("performe test:")

# test neural network
new_y = []
for i in range(len(read_json("vectors_new.json", "frequency"))):
    neuron1.update([read_json("vectors_new.json", "frequency")[i]], [w[1][0]])
    neuron2.update([1], [w[1][1]])
    neuron3.update([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
    neuron4.update([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
    neuron5.update([neuron3.y, neuron4.y], [w[3], w[4]])
    new_y.append(neuron5.y)

print(read_json("vectors_new.json", "photosynthetic_activity"))
print(new_y)
print("finished\n")
