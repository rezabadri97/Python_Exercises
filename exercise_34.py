height_lambda=lambda level_height ,ceiling_drop:level_height-ceiling_drop
calculate_clearance=height_lambda(3.2,0.45)
print(f"Clearance Report---> Effective Height: {calculate_clearance}")