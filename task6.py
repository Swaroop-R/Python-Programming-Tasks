print ("Enetr the sides of the Triangle")
x = int(input("Side 1 : "))
y = int(input("Side 2 : "))
z = int(input("Side 3 : "))
if x == y  and y == z and z == x:
    print("equilateral triangle")
elif x == y or y == z or z == x:
    print("isosceles triangle")
else:
    print("scalene triangle")
