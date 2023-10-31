class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
# Create a rectangle with length 4 and width 7
my_rectangle = Rectangle(4, 7)

# Calculate the area and perimeter
area = my_rectangle.area()
perimeter = my_rectangle.perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
