def exchange(word):
    fst = word[0]
    lst = word[-1:]
    return lst + word[1:-1] + fst

str = input("Enter your string: ")
print (exchange(str))
