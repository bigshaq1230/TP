import math

def volMasseEllipsoide(a=1, b=1, c=1, density=1):
    volume = (4/3) * math.pi * a * b * c
    mass = volume * density
    return volume, mass


print(volMasseEllipsoide())  
print(volMasseEllipsoide(2)) 
print(volMasseEllipsoide(2, 3))
print(volMasseEllipsoide(2, 3, 4))
print(volMasseEllipsoide(2, 3, 4, 0.5))