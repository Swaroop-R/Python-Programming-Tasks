x = input("Input the Filename: ")
for i in range (1,len(x)):
	if x[i]=='.':
		y=i
print(x[y+1::])