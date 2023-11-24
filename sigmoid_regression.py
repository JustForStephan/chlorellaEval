import numpy
import json

def read_json(file, key):
    f = open(file, "r")
    data = json.load(f)
    return data[key]

def write_json(file, content):
    f = open(file)
    data = json.load((f))
    data = data["linear_regression"]
    data_new = {"linear_regression":data, "sigmoid_regression": {str(estetics_in_json(content))}}

def estetics_in_json(string):                   # makes the json readable before upload
    string = string.replace("'",'"')
    string = string.replace("],","],\n")
    string = string.replace("{","{\n")
    string = string.replace("}", "\n}")
    string = string.replace(', "',',\n"')
    return string

def train_neural_network():
    pass
