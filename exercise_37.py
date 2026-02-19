class wall:
    def __init__(self, name, length, height):
        self.name=name
        self.length=length
        self.height=height
    def get_area(self):
        area=self.length*self.height
        return area
my_wall=wall("Core_Wall", 8.0, 3.5)
wall_area=my_wall.get_area()
print(f"Origin Report: {wall_area} sqm")
my_wall.height=3.0
new_area=my_wall.get_area()
print(f"Revised Report: {new_area} sqm")