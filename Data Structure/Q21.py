t = list(tuple(map(int,input("Enter tuple <x,y>: ").split(","))) for r in range(int(input('Enter number of rows: ')))) 

sorted_tuple = sorted(t, key=lambda t:t[1])

print(f'\nResult => {sorted_tuple}')