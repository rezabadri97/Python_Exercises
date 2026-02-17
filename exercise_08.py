# A list of dictionaries (Representing a Schedule)
equipment_list = [
    {"id": "M_01", "name": "  Air Handler  ", "price": 1200, "count": 2},
    {"id": "M_02", "name": "water pump", "price": 450, "count": 5},
    {"id": "M_03", "name": "  Exhaust Fan  ", "price": 300, "count": 10}
]
total_project_cost = 0
for equipment in equipment_list:
    equipment["name"]=equipment["name"].strip().upper()
    equipment["subtotal"]=equipment["price"]*equipment["count"]
    total_project_cost+=equipment["subtotal"]
    print(f"Name:{equipment["name"]} | subtotal: {equipment["subtotal"]}")
print(f"Total  Project Cost: {total_project_cost}")