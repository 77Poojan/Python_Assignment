def sortByKey():
    str = input("Enter your text : ")
    count = { }
    sortedByKeyDict = { }
    for x in str:
        if x in count.keys():
            count[x] += 1
        else:
            count[x] = 1 
        
    sortedByKeyDict = dict(sorted(count.items(), key=lambda t: t[1], reverse=True))
    print (sortedByKeyDict) 

sortByKey()