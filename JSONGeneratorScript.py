import json
import os
import pandas

# Ask filename
file_name = input("Enter JSON file name: ")

# Gets desktop path
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
completeName = os.path.join(desktop, file_name)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Ask number of input
number = 0
while True:
    number_of_input = input("Enter number of input: ")
    if number_of_input.isnumeric():
        number = int(number_of_input)
        break
    else:
        print("Input needs to be a number")

array_name_input = []
for i in range(0, number):
    temp = i+1
    array_name_input.append(input("Insert string number(%d): " % temp))


data= { }
data_array = []
for i in range(0,len(array_name_input)):
    for string in array_name_input:
        text = "Insert " + string + " for the " + str(i + 1) + " time: "
        inp = input(text)
        if is_number(inp):
            print(inp)
            data[string] = float(inp)
        else:
            data[string] = inp
    data_array.append(data)

with open(completeName + ".json", "w") as f:
    json.dump(data_array, f)