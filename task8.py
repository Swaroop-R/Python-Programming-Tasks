def total(l):
    tot = 1
    for i in l:
        tot = i *tot
    return(tot)

l = [1,5,7,3,5,4,8,9]
print(total(l))