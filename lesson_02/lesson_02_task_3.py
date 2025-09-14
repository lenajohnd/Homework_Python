import math


def square(side):
    area = side * side
    return math.ceil(area)


print(square(5))
print(square(3.2))
