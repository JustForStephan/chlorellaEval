import matplotlib.pyplot
import json

def read_json_accuracy(file, model, name):
    f = open(file, "r")
    data = json.load(f)
    subdata = data[model]
    f.close()
    return subdata[name]

def read_json(file, name, subkey):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data[subkey][name]

def lin_regression():
    input_frequency1 = read_json("input_data.json", "frequency1", "specific_regression_linear")
    input_frequency2 = read_json("input_data.json", "frequency2", "specific_regression_linear")
    output_activity1 = read_json("input_data.json", "photosynthetic_activity1", "specific_regression_linear")
    output_activity2 = read_json("input_data.json", "photosynthetic_activity2", "specific_regression_linear")
    calc_activity1 = read_json_accuracy("accuracy.json", "linear_regression", "photosynthetic_activity_calc1")
    calc_activity2 = read_json_accuracy("accuracy.json", "linear_regression", "photosynthetic_activity_calc2")

    # plot the different diagrams
    show([input_frequency1, input_frequency1], [output_activity1, calc_activity1], "Light frequency 1 and network output in dependence to photosynthetic activity","Frequency 1 of light in hz", "Photosynthetic activity in mol(O2)/(g*s)")
    show([input_frequency2, input_frequency2], [output_activity2, calc_activity2], "Light frequency 2 and network output in dependence to photosynthetic activity", "Frequency 1 of light","Photosynthetic activity")
    show([input_frequency1, input_frequency2], [output_activity1, output_activity2],"Comparison of both natural photosynthetic activity to frequencies 1 and 2", "Frequency of the light", "Photosynthetic activity")
    show([input_frequency1, input_frequency2], [calc_activity1, calc_activity2], "Comparison of the results of the neural network", "Frequency of light", "Calculated photosynthetic activity")

def sigmoid_regression():
    input_frequency = read_json("input_data.json", "frequency", "specific_regression_sigmoid")
    natural_activity_frequency = read_json("input_data.json", "photosynthetic_activity", "specific_regression_sigmoid")
    calculated_activity_frequency = read_json_accuracy("accuracy.json","sigmoid_regression", "photosynthetic_activity_calc_frequency")
    input_current = read_json("input_data.json", "input_current", "specific_regression_sigmoid")
    natural_activity_current = read_json("input_data.json", "photosynthetic_activity_by_input_current", "specific_regression_sigmoid")
    calculated_activity_current = read_json_accuracy("accuracy.json", "sigmoid_regression", "photosynthetic_activity_calc_current")
    print(calculated_activity_current)
    print(natural_activity_current)
    show([input_frequency, input_frequency],[natural_activity_frequency, calculated_activity_frequency], "Natural dependency between light frequency and photosynthetic activity in relation to calculation", "Frequency of light in hz", "Photosynthetic activity in mol(O2)/(g*s)")
    show([input_current, input_current], [natural_activity_current, calculated_activity_current], "Natural dependency between lamp current and photosynthetic activity in relation to calculation", "Current of the lamp in Ampere", "Photosynthetic activity in mol(O2)/(g*s)")

def general_regression():
    input_light = read_json_accuracy("accuracy.json", "general_regression", "input_light")
    input_co2 = read_json_accuracy("accuracy.json", "general_regression", "input_co2")
    input_temperature = read_json_accuracy("accuracy.json", "general_regression", "input_temp")
    output_capacity = read_json_accuracy("accuracy.json", "general_regression", "natural_capacity")
    network_output = read_json_accuracy("accuracy.json", "general_regression", "network_capacity")

    show([input_light, input_light], [output_capacity, network_output], "General regression: Light intensity to the CO2 capture capacity of the chorella algae", " light intensity in LUX", "CO2 capture capacity in g/(L*d)")
    show([input_temperature, input_temperature], [output_capacity, network_output], "General regression: Ambient temperature to the CO2 capture capacity of the chorella algae", "Ambient Temperature in °C", "CO2 capture capacity in g/(L*d)")
    show([input_co2, input_co2], [output_capacity, network_output], "General_regression: CO2-proportion in air to CO2 capture capacity of the chorella algae", "CO2-proportion in air in L/%", "CO2 capture capacity in g/(L*d)")
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
if regression_model == "general_regression":
    general_regression()
