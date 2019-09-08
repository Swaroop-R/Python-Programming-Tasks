numbers = [65,58,4,754,7,8,25,4,6,39,28,2,83,72,8,63,8,52,9,41,8,2,8,5,]
odd = 0
even = 0
for x in numbers:
    if not x % 2:
        even+=1
    else:
        odd+=1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)