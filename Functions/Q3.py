from operator import mul
from functools import reduce

lst = []
num = int(input("Enter number of items in list: "))
for i in range(0, num): 
    ele = int(input(f'Enter {i} index element: ')) 
    lst.append(ele) # adding the element 

def productNumber(lst):
     return reduce(lambda x, y: x * y, lst)

total = productNumber(lst)
print(f'Product: {total}');

