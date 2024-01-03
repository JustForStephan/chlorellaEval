import json
import numpy as np

def read_json(name):
    f = open("input_data.json", "r")
    data = json.load(f)
    f.close()
    return data["specific_regression_linear"][name]

def estetics_in_json(string):                   # makes the json readable before upload
    string = string.replace("'",'"')
    string = string.replace("],","],\n")
    string = string.replace("{","{\n")
    string = string.replace("}", "\n}")
    string = string.replace(', "',',\n"')
    return string

def write_json(name, data):
    f = open(name, "w")
    f.write(estetics_in_json(data))
    f.close()

def training_neural_network():

    w = [[0,0], [0,0]]
    x1 = read_json("frequency1")
    x2 = read_json("frequency2")
    y_origin1 = read_json("photosynthetic_activity1")
    y_origin2 = read_json("photosynthetic_activity2")
    eta = read_json("etha")

    print("Start training of neural network:")
    print("---------------------------------")
    for running_index in range(read_json("running_time_training")):
        for i in range(len(x1)):
            y1 = float(x1[i])*w[0][0] +w[0][1]
            y2 = float(x2[i])*w[1][0] +w[1][1]
            error1 = float(y_origin1[i])-y1
            error2 = float(y_origin2[i])-y2
            w[0][0] += float(2*error1*x1[i])    * eta
            w[0][1] += float(2*error1)          * eta
            w[1][0] += float(2*error2 * x2[i])  * eta
            w[1][1] += float(2*error2)          * eta
        print("-------------------------------------------")
        print("w11: "+str(w[0][0])+ "|  w12: "+str(w[0][1]))
        print("w21: "+str(w[1][0])+ "|  w22: "+str(w[1][1]))
        print("-------------------------------------------")

    print("final neural weight configuration: "+str(w))
    return w

w = training_neural_network() # setting neural network and train weights 1 and 2 with frequency vectors and photosynthetic_activity vectors

# safe weights
print("\nWeights get stored")
weight_data = {"linear_regression": {"w11": w[0][0], "w12": w[0][1], "w21": w[1][0], "w22": w[1][1]}}
write_json("weights.json", str(weight_data))

# calculate the difference between the calculated photosynthetic_activity and the real photosynthetic_activity (quality check)
photosynthetic_activity_calc1 = []
photosynthetic_activity_calc2 = []

for i in range(len(read_json("frequency1"))):

    calculatedY1 = read_json("frequency1")[i] * w[0][0] + w[0][1]   # calculate a photosynthetic_activity with the frequency and the weight (should be equal to the photosynthetic_activity in the dataset
    calculatedY2 = read_json("frequency2")[i] * w[1][0] + w[1][1]

    photosynthetic_activity_calc1.append(calculatedY1)
    photosynthetic_activity_calc2.append(calculatedY2)

sum_real_y = 0
sum_calc_y = 0
for y in read_json("photosynthetic_activity1"): sum_real_y += y
for z in photosynthetic_activity_calc1: sum_calc_y += z

print(sum_calc_y)
print(sum_real_y)
averageAccuracyPercent = 100 - np.abs(sum_calc_y - sum_real_y)/sum_real_y*100

data = {"linear_regression": {"photosynthetic_activity_calc1": photosynthetic_activity_calc1, "photosynthetic_activity_calc2": photosynthetic_activity_calc2, "average_accuracy": averageAccuracyPercent}}
write_json("accuracy.json", str(data))
print("\nThe difference between the real y and the calculated y:")
print("-------------------------------------------------------")
print("Average accuracy: "+ str(averageAccuracyPercent)+"%")

print("\nAlgorithm finished")
