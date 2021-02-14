str = input("Enter your text : ")
if len(str)<2:
    print("Empty String")
else:    
    firstTwoString = str[0]+str[1] 
    secondTwoString = str[-2]+str[-1]
    print (firstTwoString+secondTwoString)
