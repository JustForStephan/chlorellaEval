import json
from neurons import neuron
import random

w = [
    [1,1],
    [random.random(), random.random()],
    [random.random(), random.random()],
    [random.random()],
    [random.random()]
]

def read_json(file, name):
    f = open(file, "r")
    data = json.load(f)
    return data[name]

neuron1 = neuron([read_json("vectors_new.json", "frequency")[0]], [w[0][0]])
neuron2 = neuron([1], w[0][1])
neuron3 = neuron([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
neuron4 = neuron([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
neuron5 = neuron([neuron3.y, neuron4.y], [w[3], w[4]])
print(neuron5.y)
# loop for training index
for running_index in range(read_json("vectors_new.json", "running_time_training")):

    # loop for length of input
    for i in range(len(read_json("vectors_new.json", "frequency"))):
        neuron1 = neuron([read_json("vectors_new.json", "frequency")[i]],[w[0][0]])
        neuron2 = neuron([1],w[0][1])
        neuron3 = neuron([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
        neuron4 = neuron([neuron1.y, neuron2.y], [w[1][1], w[2][1]])
