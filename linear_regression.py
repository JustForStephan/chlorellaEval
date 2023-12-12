import json
import numpy as np

def read_json(name):
    f = open("vectors.json", "r")
    data = json.load(f)
    f.close()
    return data[name]

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

    print("Start training of neural network:")
    print("---------------------------------")
    for running_index in range(read_json("running_time_training")):
        for i in range(len(read_json("frequency1"))):
            y1 = float(read_json("frequency1")[i])*w[0][0] +w[0][1]
            y2 = float(read_json("frequency2")[i])*w[1][0] +w[1][1]
            error1 = float(read_json("photosynthetic_activity1")[i])-y1
            error2 = float(read_json("photosynthetic_activity2")[i])-y2
            w[0][0] += float(2*error1*read_json("frequency1")[i])*read_json("etha")
            w[0][1] += float(2*error1*read_json("etha"))
            w[1][0] += float(2*error2*read_json("frequency2")[i])*read_json("etha")
            w[1][1] += float(2*error2*read_json("etha"))
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
differences1 = []
differences2 = []
photosynthetic_activity_calc = []
photosynthetic_activity_calc1 = []
photosynthetic_activity_calc2 = []

for i in range(len(read_json("frequency1"))):
    originalY1 = read_json("photosynthetic_activity1")[i]
    calculatedY1 = read_json("frequency1")[i]*w[0][0] + w[0][1]   # calculate a photosynthetic_activity with the frequency and the weight (should be equal to the photosynthetic_activity in the dataset

    originalY2 = read_json("photosynthetic_activity2")[i]
    calculatedY2 = read_json("frequency2")[i] * w[1][0] + w[1][1]

    photosynthetic_activity_calc1.append(calculatedY1)
    photosynthetic_activity_calc2.append(calculatedY2)
    photosynthetic_activity_calc.append(calculatedY1)
    photosynthetic_activity_calc.append(calculatedY2)

    differences1.append(originalY1-calculatedY1)
    differences2.append(originalY2-calculatedY2)

sum_diff = 0                                                # calculate absolute average difference between input data and calculated data
for diff in differences1: sum_diff += diff
for diff in differences2: sum_diff += diff
averageDiff = sum_diff/(len(differences1)*2)

sum_real_y = 0
sum_calc_y = 0
for y in read_json("photosynthetic_activity1"): sum_real_y += y
for y in photosynthetic_activity_calc: sum_calc_y += y

averageAccuracyPercent = 100 - np.abs(sum_calc_y - sum_real_y)/sum_real_y*100

data = {"linear_regression": {"photosynthetic_activity_calc1": photosynthetic_activity_calc1, "photosynthetic_activity_calc2": photosynthetic_activity_calc2, "difference_dataset_1": differences1, "differences_dataset_2": differences2, "average_difference_abs": averageDiff, "average_accuracy": averageAccuracyPercent}}
write_json("accuracy.json", str(data))

print("\nThe difference between the real y and the calculated y:")
print("-------------------------------------------------------")
print("Abs average difference: "+ str(averageDiff))
print("Average accuracy: "+ str(averageAccuracyPercent)+"%")

print("\nAlgorithm finished")
