def get_area(length, width):
    area=round(length*width)
    return area
room_d=[(5.2, 4.1),(3.5, 3.5),(6.0, 2.8)]
for room in room_d:
    room_area=get_area(*room)
    print(f"Room Area: {room_area}")
