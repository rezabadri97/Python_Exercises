# List of room data in a project
rooms = [
    {"number": "101", "zone": "ZONE_A", "area": 12.5, "status": "Draft"},
    {"number": "102", "zone": "ZONE_B", "area": 18.0, "status": "Draft"},
    {"number": "103", "zone": "ZONE_A", "area": 15.2, "status": "Draft"},
    {"number": "201", "zone": "ZONE_C", "area": 22.0, "status": "Draft"},
    {"number": "202", "zone": "ZONE_A", "area": 10.8, "status": "Draft"}
]

target_zone = "ZONE_A"
audited_rooms = []
total_area_zone_a = 0
for room in rooms:
    if room["zone"]==target_zone:
        room["status"]="Approved"
        total_area_zone_a+=room["area"]
        audited_rooms.append(room)
print(f"Area of Zone A: {total_area_zone_a}")
for new_room in audited_rooms:
    print(f"Room Number: {new_room['number']}| Status: {new_room['status']}")