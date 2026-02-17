# List of various project elements
project_data = [
    {"id": "STR_01", "name": "Column_C1", "level": "L1"},
    {"id": "ARC_01", "name": "Wall_Exterior", "level": "L2"},
    {"id": "STR_02", "name": "Column_C2", "level": "L1"},
    {"id": "MEP_01", "name": "Pipe_Main", "level": "L3"}
]

search_keyword = "Column" # کلمه‌ای که کاربر جستجو می‌کند
results = []
for data in project_data:
    if search_keyword in data["name"]:
        results.append(data)
print(f"Results:{len(results)}")
for result in results:
    print(f"ID:{result['id']}")
    print(f"Level:{result['level']}")