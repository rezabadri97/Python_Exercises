class Wall:
    def __init__(self,name,length,height):
        self.name=name
        self.length=length
        self.height=height
    def get_area(self):
        wall_area=self.length*self.height
        return wall_area
class Curtainwall(Wall):
    def __init__(self, name, length, height,panel_count):
        super().__init__(name,length,height)
        self.panel_count=panel_count
    def get_area(self):
        wall_area=self.length*self.height*0.95
        return wall_area
facade=Curtainwall("Main_Facade", 20.0, 4.0, 10.0)
facade_area=facade.get_area()
print(f"Facade Area: {facade_area}")