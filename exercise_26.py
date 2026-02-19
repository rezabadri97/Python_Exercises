columns_bases = [
    (10, 20, 0),    # ستون اول
    (15, 20, -3),   # ستون دوم
    (10, 30, 0),    # ستون سوم
    (25, 30, -5)    # ستون چهارم
]
for column in columns_bases:
    if column[2]<0:
        print(f"Warning: Column is underground! X={column[0]} | Y= {column[1]}")
    else:
        print("Safe: Column in on or above ground")
        