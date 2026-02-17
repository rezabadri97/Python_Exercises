# A list of wall dictionaries
walls = [
    {"id": "W01", "material": "Brick", "status": "To_Be_Replaced"},
    {"id": "W02", "material": "Concrete", "status": "Approved"},
    {"id": "W03", "material": "Brick", "status": "To_Be_Replaced"},
    {"id": "W04", "material": "Steel", "status": "Approved"}
]

updates_count = 0
for wall in walls:
    if wall["status"]=="To_Be_Replaced":
        wall["material"]="Concrete"
        wall["status"]="Updated"
        updates_count+=1
print(walls)
print(f"Total walls updated: {updates_count}")