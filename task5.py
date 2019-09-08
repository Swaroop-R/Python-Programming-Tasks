mon = input("Enter the Month (use lower case) : ")
if mon in ["january","march","may","july","august","october","december"]:
    print("No. of Days : 31" )
elif mon in ["april","june","september","november"]:
    print("No of Days : 30")
elif mon == "feburary":
    print ("No of Days : 28 or 29" )
else:
    print ("Wrong Entry")