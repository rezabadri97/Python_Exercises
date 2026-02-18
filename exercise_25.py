import csv
total_cost=0
with open("material_list.csv","r") as my_file:
    reader=csv.reader(my_file)
    next(reader)
    for row in reader:
        quantity=int(row[1])
        price=float(row[2])
        total_cost+=int(quantity*price)
with open("project_summary","w") as new_file:
    writer=csv.writer(new_file)
    new_file.write(f"Project: Material Purchase\n Total Calculated Budget: {total_cost} USD\n Status: Ready for Payment")
    print("Report Generated Successfuly")