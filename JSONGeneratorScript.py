import json
import os
import pandas

# Ask filename
file_name = input("Enter JSON file name: ")

# Gets desktop path
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
completeName = os.path.join(desktop, file_name)

# Function to detect if string is a number


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Ask number of input and checks if is an actual number
number = 0
while True:
    number_of_input = input("Enter number of input: ")
    if number_of_input.isnumeric():
        number = int(number_of_input)
        break
    else:
        print("Input needs to be an integer")

# Ask for all name in the dictionary
array_name_input = []
for i in range(0, number):
    temp = i+1
    array_name_input.append(input("Insert string number(%d): " % temp))

# For each of the string he puts in, we ask the data

data_array = []

for i in range(0, len(array_name_input)):
    data = {}
    for string in array_name_input:
        text = "Insert " + string.upper() + " for the " + str(i + 1).upper() + " time: "
        result = input(text)
        if is_number(result):
            data[string] = float(result)
        else:
            data[string] = result
    data_array.append(data)


# Write on desktop with filename as the name of the file
with open(completeName + ".json", "w") as f:
    json.dump(data_array, f)

