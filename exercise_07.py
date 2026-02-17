door_info={"door_name":"internal_door","width":900,"count":5}
door_info["door_name"]=door_info["door_name"].strip().upper
door_info["total_width"]=door_info["width"]*door_info["count"]
for key,value in door_info.items():
    print(f"Parameters: {key}--->{value}")
