# Area and Circumference of a circle
import math


def areaAndCircumference(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return area, circumference


if __name__ == '__main__':
    print('#-- Area and Circumference of a Circle -- #')
    radius_str = input("Enter the radius of your circle: ")
    radius = int(radius_str)
    area, circumference = areaAndCircumference(radius)
    print("Circumference: ", circumference, "\nArea: ", area)
