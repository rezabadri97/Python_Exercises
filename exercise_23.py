import csv
header=["Item", "Quantity", "Price"]
rows = [
 ["Cement", 50, 120],  # ردیف اول: نام جنس، تعداد، قیمت
    ["Steel", 10, 850],   # ردیف دوم
    ["Brick", 2000, 0.5]  # ردیف سوم
]
with open("material_list.csv","w",newline="") as my_file:
    writer=csv.writer(my_file)
    writer.writerow(header)
    writer.writerows(rows)
