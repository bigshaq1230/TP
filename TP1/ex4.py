from math import sqrt,pi
a = int(input("lenght"))
b = int(input("height"))

print("area of rectangle, ",a*b)

if(a == b):
    print("this is a sqaure")


diameter = sqrt(a+b)
print("diameter: %.2f" %diameter)
print('enstruction: diameter: %.2f" %diameter')

R = int(input("raduis: "))
volume = pi*R*R * a

print("volume: ", volume)
