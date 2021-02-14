import functools

my_list=[]
num =int(input("Enter size of your list: "))

for i in range(0,num):
    elements = int(input(f'\nEnter the element<{i}> for your list: '))
    my_list.append(elements)

mul = functools.reduce(lambda x,y : x*y, my_list)
print(f'\nThe result is {mul}')