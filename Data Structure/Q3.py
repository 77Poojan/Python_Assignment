str = input("Enter your text : ")
front = str[0:1]
fromSecondCharacter = str[1:]
back = fromSecondCharacter.replace(front,'$')
print(front+back)
    