import numpy
import json

def read_json(file, key):
    f = open(file, "r")
    data = json.load(f)
    return data[key]

def train_neural_network():
    pass
