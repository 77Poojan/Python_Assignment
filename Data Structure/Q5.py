str = input("Enter your text : ")
if len(str)<3:
    print(str)
else:
    x = "ing"
    y = "ly"
    a = str[-3:]
    if(x == a):
        newString = str + "ly"
    else:
        newString = str + "ing"
    print (newString)   
        