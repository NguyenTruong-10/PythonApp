class Rectangle():
    def __init__(self, width, length):
        self.width =width
        self.length = length
    def Cal_S(self):
        return self.width * self.length
    def Cal_Area(self):
        return 2 * ( self.width + self.length)
    
rectangle =  Rectangle(5,7)
print(rectangle.Cal_S())
print(rectangle.Cal_Area())