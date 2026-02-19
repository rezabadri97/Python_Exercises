wall_thicknesses_list = [20, 15, 20, 30, 15, 10, 20, 30, 40, 10, 15]
new_thicknesses=set(wall_thicknesses_list)
new_thicknesses.add(25)
print(f"Report : We have {len(new_thicknesses)} unique wall thicknesses on this level. They are {new_thicknesses}")
