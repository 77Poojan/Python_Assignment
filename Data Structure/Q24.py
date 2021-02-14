my_list=[]
num =int(input("Enter size of your list: "))

for i in range(0,num):
    elements = int(input(f'\nEnter the element<{i}> for your list: '))
    my_list.append(elements)

copy_list = my_list.copy()
print (copy_list)