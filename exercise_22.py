import json
with open ("data.json","r")as my_file:
    new_data=json.load(my_file)
print(new_data["name"])