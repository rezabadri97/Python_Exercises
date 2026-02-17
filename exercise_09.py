# List of structural elements
elements = [
    {"type": "Column", "material": "Concrete", "height": 3.5},
    {"type": "Beam", "material": "Steel", "height": 0.5},
    {"type": "Column", "material": "Steel", "height": 4.2},
    {"type": "Wall", "material": "Concrete", "height": 3.0},
    {"type": "Column", "material": "Concrete", "height": 2.8}
]

concrete_columns = []
tall_elements_count = 0
for element in elements:
    if element["type"]=="Column" and element["material"]=="Concrete":
        concrete_columns.append(element)
    if element["height"]>3.0:
        tall_elements_count+=1
print(f"Concrete Columns Count:{len(concrete_columns)}")
print(f"Elements with Height more than 3 meters:{tall_elements_count}")
print(f"Concrete Columns List:{concrete_columns}")