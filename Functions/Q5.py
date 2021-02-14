import math
from math import factorial

def facto_num(number):
    return factorial(number)

num = int(input("Enter a number: "))
x = facto_num(num)
print (f'Factorial of {num} : {x}') 