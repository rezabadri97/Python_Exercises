import csv
total_cost=0
with open("material_list.csv","r") as my_file:
    reader=csv.reader(my_file)
    next(reader)
    for material in reader:
        quantity=int(material[1])
        price=float(material[2])
        total_cost+=quantity*price
print(total_cost)