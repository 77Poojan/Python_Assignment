list_strings = ['abc','xyz','aba','1221']
count = len(list(filter(lambda x:len(x)>2 and x[0]==x[-1],list_strings)))
print (count)