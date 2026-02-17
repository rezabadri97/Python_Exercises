# List of families in the project
families = [
    {"category": "Furniture", "name": "Office_Chair_A", "weight_kg": 15},
    {"category": "Lighting", "name": "Studio_Lamp", "weight_kg": 5},
    {"category": "Furniture", "name": "Office_Desk_B", "weight_kg": 45},
    {"category": "Plumbing", "name": "Sink_Type_01", "weight_kg": 12},
    {"category": "Furniture", "name": "Dining_Table_Large", "weight_kg": 80}
]

search_term = "Office" 
results_list = []
total_weight = 0
for family in families:
    if search_term in family["name"]:
        results_list.append(family)
        total_weight+=family["weight_kg"]
print(f"Found items count:{len(results_list)}")
for result in results_list:
    print(f"Category: {result['category']}")
print(f"Total Weight: {total_weight}")