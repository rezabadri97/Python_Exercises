revit_categories={"Wall":"OST_Walls","Door" : "OST_Doors","Window" : "OST_Windows","Room" : "OST_Rooms"}
for key,value in revit_categories.items():
    print(f"To collect {key}s from the database, you must use BuiltInCategory.{value} ")
