import json
import neurons
import random

w = [
    [1,1],
    [random.randrange(-1,1,0.1), random.randrange(-1,1,0.1)],
    [random.randrange(-1,1,0.1), random.randrange(-1,1,0.1)],
    [random.randrange(-1,1,0.1)],
    [random.randrange(-1,1,0.1)]
]

def read_json(file, name):
    f = open(file, "r")
    data = json.load(f)
    return data[name]


# loop for training index
for running_index in range(read_json("vectors_new.json", "running_time_training")):

    # loop for length of input
    for i in range(len(read_json("vectors_new.json", "frequency"))):
        neuron1 = neurons([read_json("vectors_new.json", "frequency")[i]],[w[0][0]])
        neuron2 = neurons([1],w[0][1])
        neuron3 = neurons([neuron1.y, neuron2.y], [w[1][0], w[2][0]])
        neuron4 = neurons([neuron1.y, neuron2.y], [w[1][1], w[2][1]])