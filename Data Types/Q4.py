firstString = input("Enter your first text : ")
secondString = input("Enter your second text : ")
newFirstString = firstString[0:2] + secondString[2:]
newSecondString = secondString[0:2] + firstString[2:]
print(newSecondString+" "+newFirstString)