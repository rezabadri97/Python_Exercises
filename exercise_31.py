def calculate_room_metrics(length,width):
    area=length*width
    perimeter=(length+width)*2
    return area,perimeter
A,P=calculate_room_metrics(5.0,4.0)
print(f"Metric -> Area: {A} sqm | Perimeter: {P} m")