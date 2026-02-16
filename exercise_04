# Format: "MaterialName_Quantity_UnitPrice"
raw_data = ["Concrete_50_120", "Steel_10_850", "Brick_2000_0.5", "Timber_15_200", "Concrete_30_115"]
total_concrete_cost = 0
materials_report = []
for data in raw_data:
    data=data.split("_")
    MaterialName=data[0]
    Quantity=data[1]
    UnitPrice=data[2]
    Quantity=float(Quantity)
    UnitPrice=float(UnitPrice)
    total_cost=Quantity*UnitPrice
    if MaterialName=="Concrete":
        total_concrete_cost+=total_cost
    materials_report.append((f"Item: {MaterialName} | Total Cost: {total_cost}"))
print(materials_report)
print(total_concrete_cost)
