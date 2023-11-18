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
    w = [random.randint(-1, 1), random.randint(-1, 1)]

    frequency1 = read_json("frequency1")
    frequency2 = read_json("frequency2")
    photosynthetic_activity1 = read_json("photosynthetic_activity1")
    photosynthetic_activity2 = read_json("photosynthetic_activity2")
    running_time = read_json("running_time_training")
    etha = read_json("etha")

    for running_index in range(running_time):
        for i in range(len(frequency1)):
            y1 = frequency1[i]*w[0]
            y2 = frequency2[i]*w[1]
            error1 = photosynthetic_activity1[i]-y1
            error2 = photosynthetic_activity2[i]-y2
            w[0]+= 2*error1*frequency1[i]*etha
            w[1]+= 2*error2*frequency2[i]*etha

def calc_new_photosynthetic_activity(w, newFrequency):
    newActivity = []
    for i in range(len(newFrequency)):
        newActivity.append(newFrequency[i]*w)
    return newActivity

w = training_neural_network()

newFrequency1 = read_json("frequency1")
newFrequency2 = read_json("frequency2")
print(w)
new_photoActivity1 = calc_new_photosynthetic_activity(w[0],newFrequency1)
new_photoActivity2 = calc_new_photosynthetic_activity(w[1], newFrequency2)
oldActivity1 = read_json("photosynthetic_activity1")
oldActivity2 = read_json("photosynthetic_activity2")

for i in range(len(newFrequency1)):
    print("--------------")
    print(oldActivity1[i])
    print(new_photoActivity1[i])

