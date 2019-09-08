def longest(l):
    max = len(l[0])
    for i in l:
        if (len(i) > max):
            max = len(i)
    return (max)

l = [ "Hi","How","Swaroop","Nature", "Temple" ]
print(longest(l))