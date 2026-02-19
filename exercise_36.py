class Wall:
    def __init__(self, name, length, height):
        self.name=name
        self.length=length
        self.height=height
    def get_area(self):
        area=self.length*self.height
        return area
my_wall=Wall("core_wall", 8.0, 3.5)
wall_area=my_wall.get_area()
print(f"Smart Wall Report--> Name: {my_wall.name} | Area: {wall_area} sqm")
