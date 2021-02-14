starts_with = lambda x: True if x.startswith(ch.upper()) else False
str = input("Enter a string: ")
ch = input("Enter a character: ")
print(starts_with(str.upper()))