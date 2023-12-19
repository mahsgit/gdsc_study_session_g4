class Shape:
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    def area(self):
        pass
class Rectanle(Shape):
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
        
    def area(self):
        return self.lenght*self.width
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return  self.radius*self.radius
r1=Rectanle(3,4)
c1=Circle(4)
print(r1.area())
print(c1.area())