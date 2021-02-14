d={}
n = int(input("Enter number of elememts in dictionary: "))
d = [map(int,input("Enter <key,value>: ").split(",")) for x in range(n)]
new_d = dict(d) 
 
for key,value in new_d.items():
    print (f'{key, new_d[key]}') 
    