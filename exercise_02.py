# Raw data from an unplanned model export
exported_elements = ["  wall_01 ", "column_01", "  WALL_02", "door_01", "WINDOW_01", "wall_03", "  COLUMN_02  "]
wall_list = []
project_name = "BIM_UNicorn_Project"
for item in exported_elements:
    item=item.strip().upper()
    wall=item.startswith("WALL")
    if wall==True:
        wall_list.append(item)
wall_count=len(wall_list) 
print(f"Project Name: {project_name.upper()}")
print(f"Wall Count: {wall_count}")
print(f"Wall List: {wall_list}")
if wall_count>2:
    print("Audit Status: Complex Model")
else:
    print("Audit Status: Simple Model")