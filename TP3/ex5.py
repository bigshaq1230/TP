import math

def trinome(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("2 roots",root1,",",root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("1 root",root)
    else:
        print("no roots")


trinome(1, -3, 2)
trinome(1, -2, 1)
trinome(1, 2, 3)