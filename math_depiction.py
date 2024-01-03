import matplotlib.pyplot
import json

def read_json_accuracy(file, model, name):
    f = open(file, "r")
    data = json.load(f)
    subdata = data[model]
    f.close()
    return subdata[name]

def read_json(file, name):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data[name]

def lin_regression():
    input_frequency1 = read_json("vectors.json", "frequency1")
    input_frequency2 = read_json("vectors.json", "frequency2")
    output_activity1 = read_json("vectors.json", "photosynthetic_activity1")
    output_activity2 = read_json("vectors.json", "photosynthetic_activity2")
    calc_activity1 = read_json_accuracy("accuracy.json", "linear_regression", "photosynthetic_activity_calc1")
    calc_activity2 = read_json_accuracy("accuracy.json", "linear_regression", "photosynthetic_activity_calc2")

    # plot the different diagrams
    show([input_frequency1, input_frequency1], [output_activity1, calc_activity1], "Light frequency 1 and network output in dependence to photosynthetic activity","Frequency 1 of light in hz", "Photosynthetic activity in mol(O2)/(g*s)")
    show([input_frequency2, input_frequency2], [output_activity2, calc_activity2], "Light frequency 2 and network output in dependence to photosynthetic activity", "Frequency 1 of light","Photosynthetic activity")
    show([input_frequency1, input_frequency2], [output_activity1, output_activity2],"Comparison of both natural photosynthetic activity to frequencies 1 and 2", "Frequency of the light", "Photosynthetic activity")
    show([input_frequency1, input_frequency2], [calc_activity1, calc_activity2], "Comparison of the results of the neural network", "Frequency of light", "Calculated photosynthetic activity")

def sigmoid_regression():
    input_frequency = read_json("sigmoid_regression/vectors_new.json", "frequency")
    natural_activity_frequency = read_json("sigmoid_regression/vectors_new.json", "photosynthetic_activity")
    calculated_activity_frequency = read_json("accuracy.json", "sigmoid_regression")["photosynthetic_activity_calc_frequency"]
    input_current = read_json("sigmoid_regression/vectors_new.json", "input_current")
    natural_activity_current = read_json("sigmoid_regression/vectors_new.json", "photosynthetic_activity_by_input_current")
    calculated_activity_current = read_json("accuracy.json", "sigmoid_regression")["photosynthetic_activity_calc_current"]
    print(calculated_activity_current)
    print(natural_activity_current)
    show([input_frequency, input_frequency],[natural_activity_frequency, calculated_activity_frequency], "Natural dependency between light frequency and photosynthetic activity in relation to calculation", "Frequency of light in hz", "Photosynthetic activity in mol(O2)/(g*s)")
    show([input_current, input_current], [natural_activity_current, calculated_activity_current], "Natural dependency between lamp current and photosynthetic activity in relation to calculation", "Current of the lamp in Ampere", "Photosynthetic activity in mol(O2)/(g*s)")

# func that shot plot
def show(x, y, title, xLabel, yLabel):
    mpl = matplotlib.pyplot
    mpl.title(title)
    mpl.xlabel(xLabel)
    mpl.ylabel(yLabel)
    mpl.plot(x[0],y[0],"o")
    mpl.plot(x[1],y[1],"o")
    mpl.plot(x[0],y[0])
    mpl.plot(x[1],y[1])
    mpl.show()

# asks for regression model
regression_model = ""
while True:
    try:
        regression_model = input("Enter the regression model you want to analyse:")
        f = open("accuracy.json", "r")
        data = json.load(f)
        data[regression_model]
        break
    except KeyError:
        print("Regression model not found, repeat the input")

if regression_model == "linear_regression":
    lin_regression()
if regression_model == "sigmoid_regression":
    sigmoid_regression()
