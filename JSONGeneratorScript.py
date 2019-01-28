import json
import os

# Ask filename
file_name = input("Please enter name file: ")

# Gets desktop path
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
completeName = os.path.join(desktop, file_name)

# Json data
data= { }
data["key"] = "value"
data["key2"] = "value2"
json_data = json.dumps(data)


# Saves to file
with open(completeName + ".json", "w") as f:
    json.dump(data, f)


