import json
import random
import numpy

def read_json(name):
    f = open("vectors.json", "r")
    data = json.load(f)
    return data[name]

def estetics_in_json(string):                   # makes the json readable before upload
    string = string.replace("'",'"')
    string = string.replace("],","],\n")
    string = string.replace("{","{\n")
    string = string.replace("}", "\n}")
    string = string.replace(', "',',\n"')
    return string

def training_neural_network():

    w = [float(random.randrange(-1, 1)), float(random.randint(-1, 1))]

    print("Start training of neural network:")
    print("----------------------------------")
    for running_index in range(read_json("running_time_training")):
        for i in range(len(read_json("frequency1"))):
            y1 = float(read_json("frequency1")[i])*w[0]
            y2 = float(read_json("frequency2")[i])*w[1]
            error1 = float(read_json("photosynthetic_activity1")[i])-y1
            error2 = read_json("photosynthetic_activity2")[i]-y2
            w[0]+= 2*error1*read_json("frequency1")[i]*read_json("etha")
            w[1]+= 2*error2*read_json("frequency2")[i]*read_json("etha")
        print("running_index: "+str(running_index))
        print("\nw1: "+str(w[0]))
        print("w2: "+str(w[1]))
    print("final neural weight configuration: "+str(w))
    return w

def calc_new_photosynthetic_activity(w, newFrequency):
    newActivity = []
    for i in range(len(newFrequency)):
        newActivity.append(newFrequency[i]*w)
    return newActivity

w = training_neural_network()

new_photoActivity1 = calc_new_photosynthetic_activity(w[0], read_json("frequency1"))
new_photoActivity2 = calc_new_photosynthetic_activity(w[1], read_json("frequency2"))

for i in range(len(read_json("frequency1"))):
    print("--------------")
    print(read_json("photosynthetic_activity1")[i])
    print(str(read_json("frequency1")[i]*w[0]))