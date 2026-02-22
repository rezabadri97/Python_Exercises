import csv
total_area=0
with open('room_schedule.csv','r') as my_file:
    reader=csv.reader(my_file)
    next(reader)
    for row in reader:
        area=float(row[1])
        total_area+=area
print(f"Report-->Total Area of all rooms: {total_area}")