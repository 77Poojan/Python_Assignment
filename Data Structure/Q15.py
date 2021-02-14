def insert_string_middle(str, middle):
    pos=len(str)//2 #<floor division>
    return str[:pos]+middle+str[pos:]

str = input("Enter the input: ")
middleString = input("Enter the message to be inserted: ")
print(insert_string_middle(str, middleString))