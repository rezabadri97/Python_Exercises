import clr
from System.Collections.Generic import List
from System import Int32
room_name=[101, 102, 103, 201, 202]
csharp_room_name=List[Int32]()
for room in room_name:
    csharp_room_name.Add(room)
print(f"Success: Added {csharp_room_name.Count} room numbers to the .NET database.")