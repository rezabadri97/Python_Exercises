def analyze_zone_area(*areas):
    total_area=0
    for area in areas:
        total_area+=area
    if total_area>150.0:
         zone_type="Large Zone"
    else:
        zone_type="Standard Zone"
    return total_area,zone_type
T_A,Z_T=analyze_zone_area(45.5, 60.0, 52.5)
print(f"Zone Report---> Total Area: {T_A} | Classification: {Z_T}")