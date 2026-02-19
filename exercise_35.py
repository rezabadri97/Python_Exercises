class Wall:
    def __init__(self,length,name,height):
        self.length=length
        self.name=name
        self.height=height
wall_1=Wall(10.5,"Exterior_W1",3.2)
wall_2=Wall(5,"Interior_W2",2.8)
print(f"Wall Report-> Name: {wall_1.name} | Area: {wall_1.length*wall_1.height}")
print(f"Wall Report-> Name: {wall_2.name} | Area: {wall_2.length*wall_2.height}")