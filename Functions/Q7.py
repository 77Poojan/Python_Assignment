def calc(s):
    upper = [i for i in s if i.isupper()]
    lower = [i for i in s if i.islower()]
    print(f' No. of Upper case characters : ',len(upper),'\n','No. of Lower case Characters : ',len(lower))

str = input("Enter a string: ")
calc(str)
