def calculate_total_area(*areas):
    total=0
    for area in areas:
        total+=area
    return total
project_A_area=calculate_total_area(12.5,15.0,20.5)
print(f"Project A TOtal Area: {project_A_area}")
project_B_area = calculate_total_area(10, 10, 15, 12, 8)
print(f"Project B Total Area: {project_B_area}")