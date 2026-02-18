import json
room_info={
    "id":101,
    "name":"Office",
    "area":25.5}
with open("data.json","w") as my_file:
    json.dump(room_info,my_file, indent=4)