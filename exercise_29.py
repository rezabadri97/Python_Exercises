def calculate_wwr(wall_area,window_area):
    wwr=(window_area/wall_area)*100
    return wwr
Room_01_wwr=calculate_wwr(50,12)
if Room_01_wwr>20:
    print(f"Warning: WWR is {Room_01_wwr}%.It is too high for energy efficiency")
else:
    print(f"Pass: WWR is {Room_01_wwr}%. Good Job!")
    