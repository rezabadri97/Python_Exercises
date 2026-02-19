room_areas = [15.5, 9.2, 20.0, 11.5, 35.0, 8.0, 12.0]
standard_rooms = []
for area in room_areas:
    if area>=12:
        standard_rooms.append(area)
        print(f"Pass: Room size {area} sqm is standard.")
    else:
        print(f"Warning: Room size {area} sqm is below standard!")
print(f"We have {len(standard_rooms)} standard rooms. List:{standard_rooms}")