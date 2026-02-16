# Raw opening data: [Name:Width_in_mm]
raw_openings = ["D01:800", "  d02:1050 ", "D03:900", "  D04:1200  ", "w01:1500"]
standard_doors = []
wide_doors = []
for item in raw_openings:
    item=item.strip().upper()
    item=item.split(":")
    id=item[0]
    width=item[1]
    width=int(width)
    if id.startswith("W"):
        continue
    if width > 1000:
        wide_doors.append(id)
    else:
        standard_doors.append(id)
print(f"Wide Doors:{wide_doors}")
print(f"Wide Doors Count:{len(wide_doors)}")