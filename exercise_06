# Raw Data Format -> "FloorNumber|RoomType|AreaSQM"
raw_floor_data= [
    "01|LIVING_ROOM|35.5", 
    " 01|KITCHEN|12.0 ", 
    "02|Bedroom_Master|28.5", 
    "01|BALCONY|5.0", 
    "02|BEDROOM_02|18.2", 
    "03|Penthouse_Main|120.0", 
    "02|  BALCONY  |4.5"
    ]
total_residential_area = 0
balcony_list = []
project_status = "PRELIMINARY"
for item in raw_floor_data:
    clear_data=item.strip().upper()
    clear_data=clear_data.split("|")
    floor=int(clear_data[0])
    room_type=clear_data[1].strip()
    area=float(clear_data[2].strip())
    if room_type.startswith("BALCONY"):
         balcony_list.append(room_type)
    balcony_count=len(balcony_list)
    if floor<3:
        total_residential_area+=area
print("-------------------")
print(f"Balcony Count: {balcony_count}")
print(f"Balcony List:{balcony_list}")
print(f"Total Residental Area: {total_residential_area}")
if total_residential_area>80 and balcony_count>=2:
     print("Status: READY_FOR_SUBMISSIN")
    