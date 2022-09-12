def right_trinle(p, b, h):
    if (h**2 == (p**2+b**2)):
        print("triangle is right triangle")
    else:
        print("triangle is not right triangle")


p = int(input("enter the perpendicular of triangle:"))
b = int(input("enter the base of triangle:"))
h = int(input("enter the hypotenus of trianle:"))
right_trinle(p, b, h)
