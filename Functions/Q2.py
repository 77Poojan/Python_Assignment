lst = []
num = int(input("Enter number of items in list: "))
for i in range(0, num): 
    ele = int(input(f'Enter {i} index element: ')) 
    lst.append(ele) # adding the element 

def sumNumber(lst):
    return sum(lst)

total = sumNumber(lst)
print(f'Sum: {total}');

