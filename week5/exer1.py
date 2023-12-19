# class Rectangle:
#     def __init__(self,length,width) :
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return (self.length + self.width)*2
# r1=Rectangle(3.0,4.9)
# print("the area is :", r1.area())
# print("the perimeter :",r1.perimeter())



from abc import   ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
    
class Shape:
    def __init__(self,color):
        self.color=color
    def get_color(self):
        return self.color
    
    @abstractmethod
    def area(self):
        pass
        
class Rectanle(Shape):
    def __init__(self,lenght,width,color):
        super().__init__(color)
        self.lenght=lenght
        self.width=width
        
    def area(self):
        return self.lenght*self.width
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return  self.radius*self.radius
r1=Rectanle(3,4, "black")
c1=Circle(4)
r1.get_color()
print(r1.area())
print(c1.area())

    
    
 
