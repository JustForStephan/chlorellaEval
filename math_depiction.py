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

def lin_regression(regression_type):
    input_frequency1 = read_json("vectors.json", "frequency1")
    input_frequency2 = read_json("vectors.json", "frequency2")
    output_activity1 = read_json("vectors.json", "photosynthetic_activity1")
    output_activity2 = read_json("vectors.json", "photosynthetic_activity2")
    calc_activity1 = read_json_accuracy("accuracy.json", regression_type, "photosynthetic_activity_calc1")
    calc_activity2 = read_json_accuracy("accuracy.json", regression_type, "photosynthetic_activity_calc2")

    #plot with the first frequency
    plot1 = matplotlib.pyplot
    plot1.plot(input_frequency1,output_activity1,"o")
    plot1.plot(input_frequency1,calc_activity1)

    plot1.plot(input_frequency1,output_activity1)
    plot1.plot(input_frequency1,calc_activity1, "o")

    plot1.title("Light frequency 1 and network output in dependence to photosynthetic activity")
    plot1.xlabel("Frequency 1 of light")
    plot1.ylabel("Photosynthetic activity")
    plot1.show()


    # plot with the second frequency
    plot2 = matplotlib.pyplot
    plot2.plot(input_frequency2, output_activity2,"o")
    plot2.plot(input_frequency2, output_activity2)

    plot2.plot(input_frequency2, calc_activity2, "o")
    plot2.plot(input_frequency2, calc_activity2)

    plot2.title("Light frequency 2 and network output in dependence to photosynthetic activity")
    plot2.xlabel("Frequency 2 of light")
    plot2.ylabel("Photosynthetic activity")
    plot2.show()

    # plot with comparison of frequencies
    plot3 = matplotlib.pyplot
    plot3.plot(input_frequency1, output_activity1,"o")
    plot2.plot(input_frequency1, output_activity1)

    plot3.plot(input_frequency2, output_activity2, "o")
    plot3.plot(input_frequency2, output_activity2)

    plot3.title("Light frequency 1 and 2 in dependence to photosynthetic activity")
    plot3.xlabel("Frequency 2 of light")
    plot3.ylabel("Photosynthetic activity")
    plot3.show()


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
    lin_regression("linear_regression")
