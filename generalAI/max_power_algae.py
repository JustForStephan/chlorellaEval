from neurons import neuron
import json

def estetics_in_json(string):                   # makes the json readable before upload
    string = string.replace("'",'"')
    string = string.replace("],","],\n")
    string = string.replace("{","{\n")
    string = string.replace("}", "\n}")
    string = string.replace(', "',',\n"')
    return string

# create input data shapes
input_light = []
input_co2 = []
input_temp = []

actual_light_val = 0
actual_co2_val = 0
actual_temp_val = 0
index = 100

for i in range(index):
    actual_light_val += 4000/index * 10.0e-5
    input_light.append(actual_light_val)

    actual_co2_val += 0.2/index
    input_co2.append((actual_co2_val))

    actual_temp_val += 30/index * 1.0/100
    input_temp.append(actual_temp_val)

print(input_light)
print(input_co2)
print(input_temp)

# create neural network
i1 = neuron(); i2 = neuron(); i3 = neuron(); i4 = neuron(); h1 = neuron(); h2 = neuron(); o = neuron()

# load neural weights
f = open("./../weights.json")
data = json.load(f)
f.close()
iw = data["general_regression"]["iw"]
hw = data["general_regression"]["hw"]
ow = data["general_regression"]["ow"]

highest_conditions = []
highest_output = 0.0

for x in range(index):
    for y in range(index):
        for z in range(index):

            i1.update([input_light[x], input_co2[y], input_temp[z], 1], [iw[0][0], iw[1][0], iw[2][0], iw[3][0]])
            i2.update([input_light[x], input_co2[y], input_temp[z], 1], [iw[0][1], iw[1][1], iw[2][1], iw[3][1]])
            i3.update([input_light[x], input_co2[y], input_temp[z], 1], [iw[0][2], iw[1][2], iw[2][2], iw[3][2]])
            i4.update([input_light[x], input_co2[y], input_temp[z], 1], [iw[0][3], iw[1][3], iw[2][3], iw[3][3]])
            h1.update([i1.y, i2.y, i3.y, i4.y], [hw[0][0], hw[1][0], hw[2][0], hw[3][0]])
            h2.update([i1.y, i2.y, i3.y, i4.y], [hw[0][1], hw[1][1], hw[2][1], hw[3][1]])
            o.update([h1.y, h2.y], [ow[0][0], ow[1][0]])

            if o.y > highest_output:
                highest_output = o.y
                highest_conditions = [input_light[x], input_co2[y], input_temp[z]]
highest_conditions[0] = highest_conditions[0]*10000
highest_conditions[2] = highest_conditions[1]*100
print("Algorithm finished:")
print("Highest output: "+ str(highest_output))
print("highest conditions " + str(highest_conditions))

f = open("./../accuracy.json", "r")
data = json.load(f)
f.close()
data.update({"max_classification": {"max_capacity": highest_output, "max_conditions": highest_conditions}})

f = open("./../accuracy.json", "w")
f.write(estetics_in_json(str(data)))