def checkin(number,start,end):
    if number in range(start,end+1):
        print( f'{number} is in the range <{start} - {end}>')
    else :
        print("The number is outside the range <{start} - {end}>")

num = int(input("Enter a number: "))       
start = int(input("Enter a start: ")) 
end = int(input("Enter a end: ")) 

checkin(num,start,end)