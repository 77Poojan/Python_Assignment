my_list=[]
num =int(input("Enter size of your list: "))
s = 0
for i in range(0,num):
    elements = int(input(f'\nEnter the element<{i}> for your list: '))
    my_list.append(elements)

largest_number = max(my_list, key=lambda s: s)
print(f'\nThe result is largest number is {largest_number}')