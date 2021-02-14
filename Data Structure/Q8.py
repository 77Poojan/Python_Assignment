def nstring(str, n):
    new_str = str.replace(str[n], "")
    return new_str

str = input("Enter your text: ")
nindex = int(input("Enter deleting character index: "))
print(nstring(str,nindex))