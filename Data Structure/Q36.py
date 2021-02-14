import functools

d={}
n = int(input("Enter number of elememts in dictionary: "))
d = [map(int,input("Enter <key,value>: ").split(",")) for x in range(n)]
new_d = dict(d) 

sum = functools.reduce(lambda x,y : x+y, new_d.values())
print(f'The sum is {sum}')