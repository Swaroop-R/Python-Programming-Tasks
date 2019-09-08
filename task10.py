class rectangle:
    def area(self,l,b):
        return (l*b)
l = float(input("Enter the Length : "))
b = float(input("Enter the Breadth : "))
rectangle1 = rectangle()
print (rectangle1.area(l,b))