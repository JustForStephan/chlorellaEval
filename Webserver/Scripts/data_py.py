from neurons import neuron
import json

def run(request={}):
    input_light = float(request["light"])
    input_co2 = float(request["co2"])
    input_temp = float(request["temp"])
    # Process
    
    f = open("./weights.json")
    data = json.load(f)
    f.close()
    iw = data["general_regression"]["iw"]
    hw = data["general_regression"]["hw"]
    ow = data["general_regression"]["ow"]
    print(hw)
    print("---> finished")

    # scale data
    print("\nscale data")
    input_light = input_light * 10.0e-5
    input_co2 = input_co2 * 1.0
    input_temp = input_temp * 1.0/100
    print("---> finished")

    # create neural network
    print("\ncreate neuronal network")
    i1 = neuron(); i2 = neuron(); i3 = neuron(); i4 = neuron(); h1 = neuron(); h2 = neuron(); o = neuron()
    print("---> finished")

    # calc with respective data
    print("\nStart calculation with given data:")
    i1.update([input_light, input_co2, input_temp, 1], [iw[0][0], iw[1][0], iw[2][0], iw[3][0]])
    i2.update([input_light, input_co2, input_temp, 1], [iw[0][1], iw[1][1], iw[2][1], iw[3][1]])
    i3.update([input_light, input_co2, input_temp, 1], [iw[0][2], iw[1][2], iw[2][2], iw[3][2]])
    i4.update([input_light, input_co2, input_temp, 1], [iw[0][3], iw[1][3], iw[2][3], iw[3][3]])
    h1.update([i1.y, i2.y, i3.y, i4.y], [hw[0][0], hw[1][0], hw[2][0], hw[3][0]])
    h2.update([i1.y, i2.y, i3.y, i4.y], [hw[0][1], hw[1][1], hw[2][1], hw[3][1]])
    o.update([h1.y, h2.y], [ow[0][0], ow[1][0]])
    print("---> finished")

    # storage result in json
    data = {"result": round(o.y*10, 2)}
    return json.dumps(data)
