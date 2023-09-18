class Rectangle:

    def __init__(self, wide, high):
        self.wide = wide
        self.high = high

    def square(self):
        return self.wide*self.high

    def perimeter(self):
        return 2*(self.wide + self.high)

rectangle = Rectangle(10,2)

print(rectangle.square())
print(rectangle.perimeter())
